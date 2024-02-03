# -------------------------------------------------------------------------------------------------
# Copyright (c) 2023,2024 The beep-projects contributors
# this file originated from https://github.com/beep-projects
# Do not remove the lines above.
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see https://www.gnu.org/licenses/
# -------------------------------------------------------------------------------------------------

"""Classes to connect to Beurer blood preassure meters"""

from abc import ABC, abstractmethod
from bpm import BPM
from datetime import date, datetime
import serial
from serial import SerialException
from serial.tools.list_ports import comports
import time
from typing_extensions import override
import usb.core


class BeurerBM(ABC):
  """Abstract class for implementing Beurer blood preassure meters"""

  def __init__(self):
    self.connected = False

  @abstractmethod
  def connect(self) -> bool:
    """initialize a connection with the device"""
    pass

  @abstractmethod
  def disconnect(self) -> bool:
    """clean shut down of the connection with the device"""
    pass

  @abstractmethod
  def get_name(self) -> str:
    """get the device identifier

    Returns:
        name of the device
    """
    pass

  @abstractmethod
  def get_count(self) -> int:
    """get the number of records stored on the device

    Returns:
        Number of Records
    """
    pass

  @abstractmethod
  def get_measurement(self, num: int) -> dict[str, any] | None:
    """Get a specific measurement off the device

    Args:
        num: number of measurement to read.
            Use :func: '~BeurerBM.get_count' to get the range of valid nums

    Returns:
        dict holding the values of the measurement or None.
        The dict should have the following keys, if they are supported my the device
        'systolic' = Systolic measurement in mmHg
        'diastolic' = Diastolic measurement in mmHg
        'pulse rate' = Pulse rate of the measurement in beats per minute
        'TODO pulse pressure, date, time'
        'day' = day of the measurement date
        'month' = month of the measurement date
        'year' = year of the measurement date
        'hour' = hour of the measurement timestamp
        'minute' = minute of the measurement timestamp
        'user' = user id if supported by the device, or 0
        'irregular heart beat' = True if irregular heart beat was detected else False
        'risk index' = WHO risk assessment for this measurement
        'recommendation' = recommendation to take action based on risk index
    """
    pass


class BeurerBMSerial(BeurerBM):
  """Class to support Beurer devices using a USB to serial converter

  Devices reported to have such a converter are older versions of BM58, BC58, BM65
  When plugging thes into your Linux, they should show up as /dev/ttyUSB...

  This code is compiled from internet sources and NOT tested.
  Please contribut to the project, if you want to use this class
  """

  def __init__(self, device):
    super().__init__()
    self.device = device
    self.serialport = None

  @override
  def connect(self) -> bool:
    try:
      self.serialport = serial.Serial(
          port=self.device,
          baudrate=4800,
          parity=serial.PARITY_NONE,
          stopbits=serial.STOPBITS_ONE,
          bytesize=serial.EIGHTBITS,
          timeout=0.5,
      )
    except SerialException:
      self.connected = False
      return False
    # ping device to test connection
    self.serialport.write(b'\xAA')
    if self.serialport.read() != b'\x55':
      self.serialport.close()
      self.serialport = None
      self.connected = False
      return False
    self.connected = True
    return True

  @override
  def disconnect(self):
    self.serialport.close()
    self.serialport = None
    self.connected = False

  @override
  def get_name(self) -> str:
    self.serialport.write(b'\xA4')
    response = self.serialport.read(32).decode('ASCII')
    return response

  @override
  def get_count(self) -> int:
    self.serialport.write(b'\xA2')
    response = int.from_bytes(self.serialport.read(), byteorder='little')
    return response

  @override
  def get_measurement(self, num: int) -> dict[str, any] | None:
    self.serialport.write(b'\xA3' + num.to_bytes(1, byteorder='little'))
    if self.serialport.read() == b'\xAC':
      dataset = self.serialport.read(8)
      measurement = BPM.get_empty_measurement()
      measurement[BPM.systolic] = dataset[0] + 25
      measurement[BPM.diastolic] = dataset[1] + 25
      measurement[BPM.pulse_pressure] = measurement[BPM.systolic] - measurement[BPM.diastolic]
      measurement[BPM.pulse] = dataset[2]
      year = dataset[7] + 2000
      month = dataset[3]
      day = dataset[4]  # & 0b00011111
      hour = dataset[5]
      minute = dataset[6]
      dt = datetime(year, month, day, hour, minute)
      measurement[BPM.date] = dt.date()
      measurement[BPM.time] = dt.time()
      measurement[BPM.user] = 0  # ((dataset[4] & 0b10000000) >> 7) + 1
      measurement[BPM.irregular_heart_beat] = (
          False  # True if dataset[4] & 0b01100000 != 0 else False
      )
      idx, recommendation = BPM.get_risk_assessment(
          measurement[BPM.systolic], measurement[BPM.diastolic]
      )
      measurement[BPM.risk_index] = idx
      measurement[BPM.recommendation] = recommendation

      return measurement
    # implicit handle 0xA9 for unknown id
    return None


class BeurerBMUSB(BeurerBM):
  """Class to support Beurer devices using USB for communication

  This class was written and tested using a Beurer BM58
  If it is not working for your Beurer device, please contribut to the project
  """

  def __init__(self, vid, pid):
    super().__init__()
    self.vid = vid
    self.pid = pid
    self.usbdevice = None

  def _tx(self, data: list[int]):
    """Send data to device

    The data length is 8 bytes.
    If the data length is less than 8 byte the data is filled with 0xF4.
    """
    #  bmRequestType, bRequest, wValue=0, wIndex=0, data_or_wLength=None, timeout=None
    self.usbdevice.ctrl_transfer(
        0x21,
        0x09,
        0x0200,
        0,
        data + [0xF4, 0xF4, 0xF4, 0xF4, 0xF4, 0xF4, 0xF4],
    )

  def _rx(self, length: int):
    """Read bytes from device

    Args:
        length: the number of bytes to read

    Returns:
        the bytes read
    """
    try:
      rx = self.usbdevice.read(0x81, length)
    except usb.core.USBTimeoutError:
      return []
    return rx

  def _trim(self, data):
    """removes the padding byte 0xF4 from a byte list"""
    if data:
      while data[-1] == 0xF4:
        data.pop()
    return data

  @override
  def connect(self):
    """find the device in the usb subsystem and try to condect to it"""
    self.usbdevice = usb.core.find(idVendor=self.vid, idProduct=self.pid)
    if self.usbdevice is None:
      self.connected = False
      return False
    # Detach usbhid driver
    try:
      if self.usbdevice.is_kernel_driver_active(0):
        try:
          self.usbdevice.detach_kernel_driver(0)
        except usb.core.USBError:
          self.usbdevice = None
          self.connected = False
          return False
    except NotImplementedError:
      # this is expected to happen on windows, no action needed
      pass
    self.usbdevice.set_configuration()
    # if the device is plugged in, it needs some time before it accepts connections
    time.sleep(1)
    # ping device to check if connection is really working
    self._tx([0xAA])
    rx = self._rx(8)
    if rx and rx[0] == 0x55:
      self.connected = True
      return True
    self.connected = False
    return False

  @override
  def disconnect(self):
    # If you want to end the communication, send first
    # the 0xF7 command and after at least 40ms delay 0xF6.
    self._tx([0xF7])
    time.sleep(0.05)
    self._tx([0xF6])
    time.sleep(0.05)
    self.usbdevice.reset()
    self.usbdevice = None
    self.connected = False

  @override
  def get_name(self) -> str:
    cmd_bytes = [0xA4, 0xA5, 0xA6, 0xA7]
    rx_buf = []
    for i in cmd_bytes:
      self._tx([i])
      rx_buf += self._trim(self._rx(8))
    return bytes(rx_buf).decode('ASCII')

  @override
  def get_count(self) -> int:
    cmd_bytes = [0xA2]
    self._tx(cmd_bytes)
    return self._rx(8)[0]

  @override
  def get_measurement(self, num: int) -> dict[str, any] | None:
    # The first measurement starts with 0x01 and represents the newest measurement
    # of user 1 (highest measurement number on the device).
    # 0x02 is the second newest measurement of user 1. When all measurements of user 1 are read,
    # the next measurement is the newest measurement of user 2.
    cmd_bytes = [0xA3, num]
    self._tx(cmd_bytes)
    dataset = self._rx(8)
    if dataset[0] == 0xA9:
      # requested measurement does not exist
      return None
    measurement = BPM.get_empty_measurement()
    # documentation seems to be wrong on some of these values.
    # parsing rules for user, IHR and year are obtained by observation
    measurement[BPM.systolic] = dataset[0] + 25
    measurement[BPM.diastolic] = dataset[1] + 25
    measurement[BPM.pulse_pressure] = measurement[BPM.systolic] - measurement[BPM.diastolic]
    measurement[BPM.pulse] = dataset[2]
    year = (dataset[7] & 0b00011111) + 2000
    month = dataset[3]
    day = dataset[4] & 0b00011111
    hour = dataset[5]
    minute = dataset[6]
    dt = datetime(year, month, day, hour, minute)
    measurement[BPM.date] = dt.date()
    measurement[BPM.time] = dt.time()
    measurement[BPM.user] = ((dataset[4] & 0b10000000) >> 7) + 1
    measurement[BPM.irregular_heart_beat] = True if dataset[7] & 0b10000000 != 0 else False
    idx, recommendation = BPM.get_risk_assessment(
        measurement[BPM.systolic], measurement[BPM.diastolic]
    )
    measurement[BPM.risk_index] = idx
    measurement[BPM.recommendation] = recommendation
    return measurement


def find(device: str | None = None, timeout: int = 10) -> BeurerBM:
  """Find any Beurer blood preassure meter connected it to this machine

    First [device] is tested, if parameter is present, then
    the presence of a known usb devices is tested
    and finally all available COM ports are checked

  Args:
      device: device location for the BeurerBM
      timout: If device is not given, the search for a connected device
        on USB or COM will be done for [timeout] seconds

  Returns:
      The BeurerBM object if found or None
  """
  if device is not None and _test_serial_device(device):
    return BeurerBMSerial(device)
  # list of known (Vendor ID, Product ID) tuples
  # used for USB devices
  known_devices = [(0x0C45, 0x7406)]
  start = time.time()
  while (time.time() - start) < timeout:
    for dev_info in known_devices:
      if _test_usb_device(dev_info[0], dev_info[1]):
        return BeurerBMUSB(dev_info[0], dev_info[1])
    for dev in comports():
      if _test_serial_device(dev):
        return BeurerBMSerial(dev)
    time.sleep(1)

  return None


def _test_usb_device(vid: int, pid: int) -> bool:
  """find the device in the usb subsystem and try to condect to it"""
  usbdevice = usb.core.find(idVendor=vid, idProduct=pid)
  if usbdevice is not None:
    return True
  return False


def _test_serial_device(device: str) -> bool:
  try:
    serialport = serial.Serial(
        port=device,
        baudrate=4800,
        parity=serial.PARITY_NONE,
        stopbits=serial.STOPBITS_ONE,
        bytesize=serial.EIGHTBITS,
        timeout=0.5,
    )
  except SerialException:
    return False
  # ping device
  serialport.write(chr(0xAA))
  if serialport.read() != b'\x55':
    serialport.close()
    return False
  serialport.close()
  return True
