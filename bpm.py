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
"""Module that provides only class BPM"""
from typing import Tuple


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
  def get_risk_assessment(syst, diast) -> Tuple[int, str]:
    """get the risk idx and action recommendation for a blood pressure measurement

    Args:
      syst: systole of the measurement
      diast: diastole of the measurement

    Returns:
      idx: index of the entry in the risk_classification list
      recommendation: the recommendation of the WHO
    """
    # loop from back to front. This ensures, the highest match is returned
    for i in range(len(BPM.risk_classification) - 1, -1, -1):
      # a match is if either syst or diast is in the defined range
      if (
          BPM.risk_classification[i]['systole min'] <= syst
          and BPM.risk_classification[i]['systole max'] >= syst
      ) or (
          BPM.risk_classification[i]['diastole min'] <= diast
          and BPM.risk_classification[i]['diastole max'] >= diast
      ):
        return BPM.risk_classification[i]['idx'], BPM.risk_classification[i]['recommendation']
    return -1, 'unclassified'

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
