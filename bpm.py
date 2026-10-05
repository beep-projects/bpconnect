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
"""Module that provides only static class BPM and abstract class BloodPressureMeter"""
from typing import Tuple
from abc import ABC, abstractmethod


class BPM:
  """Class defining the structiure of a blood pressure measurment as dict

  The dict should have the following keys, if they are supported my the device
    'systolic' = Systolic measurement in mmHg
    'diastolic' = Diastolic measurement in mmHg
    'pulse rate' = Pulse rate of the measurement in beats per minute
    'TODO pulse pressure'
    'TODO date'
    'TODO time'
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

  date = 'date'
  time = 'time'
  systolic = 'systolic'
  diastolic = 'diastolic'
  pulse_pressure = 'pulse pressure'
  pulse = 'pulse rate'
  user = 'user'
  irregular_heart_beat = 'irregular heart beat'
  risk_index = 'risk index'
  recommendation = 'recommendation'

  keys = [
      date,
      time,
      systolic,
      diastolic,
      pulse_pressure,
      pulse,
      user,
      irregular_heart_beat,
      risk_index,
      recommendation,
  ]

  risk_classification = [
      {
          'idx': 0,
          'name': 'hypotension',
          'systole min': 0,
          'systole max': 100,
          'diastole min': 0,
          'diastole max': 60,
          'recommendation': 'self-monitoring',
      },
      {
          'idx': 1,
          'name': 'optimal',
          'systole min': 100,
          'systole max': 120,
          'diastole min': 60,
          'diastole max': 80,
          'recommendation': 'self-monitoring',
      },
      {
          'idx': 2,
          'name': 'normal',
          'systole min': 120,
          'systole max': 130,
          'diastole min': 80,
          'diastole max': 85,
          'recommendation': 'self-monitoring',
      },
      {
          'idx': 3,
          'name': 'high normal',
          'systole min': 130,
          'systole max': 140,
          'diastole min': 85,
          'diastole max': 90,
          'recommendation': 'regular monitoring by doctor',
      },
      {
          'idx': 4,
          'name': 'mild hypertension',
          'systole min': 140,
          'systole max': 160,
          'diastole min': 90,
          'diastole max': 100,
          'recommendation': 'regular monitoring by doctor',
      },
      {
          'idx': 5,
          'name': 'moderate hypertension',
          'systole min': 160,
          'systole max': 180,
          'diastole min': 100,
          'diastole max': 110,
          'recommendation': 'seek medical attention',
      },
      {
          'idx': 6,
          'name': 'severe hypertension',
          'systole min': 180,
          'systole max': 282,
          'diastole min': 110,
          'diastole max': 282,
          'recommendation': 'seek medical attention',
      },
  ]

  @staticmethod
  def is_complete(dictionary: dict):
    """Test if a given dict has all mandatory keys

    Attributes:
      dictionary = the dict to evaluate

    Returns:
      True if
    """
    return all(k in dictionary.keys() for k in BPM.keys)

  @staticmethod
  def get_risk_indices(syst, diast) -> Tuple[int, int]:
    """get the risk idx and action recommendation for a blood pressure measurement

    Args:
      syst: systole of the measurement
      diast: diastole of the measurement

    Returns:
      idx: index of the entry in the risk_classification list
      recommendation: the recommendation of the WHO
    """
    # loop from back to front. This ensures, the highest match is returned
    # for i in range(len(BPM.risk_classification) - 1, -1, -1):
    risk_idx_syst = -1
    risk_idx_diast = -1
    for i in range(0, len(BPM.risk_classification)):
      # a match is if either syst or diast is in the defined range
      if (
          BPM.risk_classification[i]['systole min'] <= syst
          and BPM.risk_classification[i]['systole max'] >= syst
      ):
        risk_idx_syst = i
      if (
          BPM.risk_classification[i]['diastole min'] <= diast
          and BPM.risk_classification[i]['diastole max'] >= diast
      ):
        risk_idx_diast = i
    return risk_idx_syst, risk_idx_diast

  @staticmethod
  def get_risk_recommendation(risk_index: int) -> str:
    """get the action recommendation for a given risk index

    Args:
      risk_index: the risk index for which a recommendation is wanted

    Returns:
      recommendation: the recommendation of the WHO
    """
    if risk_index in range(0, len(BPM.risk_classification)):
      return BPM.risk_classification[risk_index]['recommendation']
    return 'unclassified'

  @staticmethod
  def get_risk_assessment(syst, diast) -> Tuple[int, str]:
    """get the risk idx for systolic and diastolic values

    Args:
      syst: systole of the measurement
      diast: diastole of the measurement

    Returns:
      (int, int): tuple of (risk index systolic, risk index diastolic)
    """
    risk_idx_syst, risk_idx_diast = BPM.get_risk_indices(syst, diast)
    risk_idx = max(risk_idx_syst, risk_idx_diast)
    recommendation = BPM.get_risk_recommendation(risk_idx)
    return risk_idx, recommendation

  @staticmethod
  def get_empty_measurement() -> dict[str, any] | None:
    """Get a prototype of a measurement

    Returns:
      dict with following keys
      'systolic' = Systolic measurement in mmHg
      'diastolic' = Diastolic measurement in mmHg
      'pulse rate' = Pulse rate of the measurement in beats per minute
      'TODO pulse pressure'
      'TODO date'
      'TODO time'
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
    return {
        BPM.date: None,
        BPM.time: None,
        BPM.systolic: -1,
        BPM.diastolic: -1,
        BPM.pulse_pressure: -1,
        BPM.pulse: -1,
        BPM.user: -1,
        BPM.irregular_heart_beat: False,
        BPM.risk_index: -1,
        BPM.recommendation: '',
    }


class BloodPressureMeter(ABC):
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
