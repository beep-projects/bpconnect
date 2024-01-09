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

"""Script to read blood pressure measurements from a Beurer blood pressure meter
and upload them to Garmin Connect
"""

import argparse
from io import BytesIO
from bpm import BPM
import base64
import copy
from datetime import date, datetime, timedelta
import numpy as np
import pandas as pd
from pathlib import Path
from typing import Tuple

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from matplotlib import rcParams

from bmconnect_fonts import font_roboto, font_roboto_base64
from matplotlib.font_manager import fontManager

#fontManager.addfont(BytesIO(base64.b64decode(font_roboto_base64)).getvalue())
#fontManager.addfont(font_roboto)

data_folder = Path.home() / '.bmconnect'
data_file = data_folder / 'measurements.feather'

# general plot configuration
category_colors = ListedColormap(['khaki', 'limegreen', 'green', 'olivedrab', 'gold', 'coral', 'red'])

def _read_measurements():
  try:
    df = pd.read_feather(data_file)
  except FileNotFoundError:
    df = pd.DataFrame()
  if not all(k in list(df.columns) for k in BPM.keys):
    print("Not a valid measurement file")
    return None
  return df

def _bp_scatter_plot(df, block=True):
  """
  Generate a scatter plot of blood pressure data.

  Args:
    df (DataFrame): The input data as pandas DataFrame.

  Returns:
    scat: The scatter plot.
   """
  #df = df.reset_index()
  #print(df.to_string())
  category_systolic = [c['systole min'] for c in BPM.risk_classification]
  category_systolic.append(BPM.risk_classification[-1]['systole max'])
  # overwrite min and max
  category_systolic[0] = 50
  category_systolic[-1] = 200

  category_diastolic = [c['diastole min'] for c in BPM.risk_classification]
  category_diastolic.append(BPM.risk_classification[-1]['diastole max'])
  # overwrite min and max
  category_diastolic[0] = 20
  category_diastolic[-1] = 130

  X1d = np.arange(category_diastolic[0], category_diastolic[-1], 0.25)
  Y1d = np.arange(category_systolic[0], category_systolic[-1], 0.25)
  Xdiastole, Ysystole = np.meshgrid(X1d, Y1d)

  xvals = df[BPM.diastolic].tolist()
  yvals = df[BPM.systolic].tolist()

  backgr = np.full_like(Xdiastole, 0)
  for i in range(1,len(BPM.risk_classification)):
    backgr[((Xdiastole >= category_diastolic[i]) & (Ysystole < category_systolic[i])) | ((Xdiastole < category_diastolic[i]) & (Ysystole >= category_systolic[i])) | ((Xdiastole >= category_diastolic[i]) & (Ysystole >= category_systolic[i]))] = i

  #rcParams['font.weight'] = 'bold'
  #plt.rcParams['figure.dpi'] = 150
  #fig, ax = plt.subplots()
  fig = plt.figure()
  ax = fig.add_subplot()

  ax.scatter(xvals, yvals, color='black')
  #cmap = ListedColormap(['khaki', 'limegreen', 'green', 'olivedrab', 'gold', 'coral', 'red'])
  ax.imshow(backgr[:-1, :-1], cmap=category_colors, alpha=0.5, extent=[X1d[0], X1d[-1], Y1d[0], Y1d[-1]], origin='lower', aspect='auto')

  for i in range(1, len(category_systolic)):
    y = (category_systolic[i] + category_systolic[i-1]) / 2.0 - 2
    plt.annotate(BPM.risk_classification[i-1]['name'], (X1d[0]+2,y))

  plt.xlabel('diastolic', weight='bold')
  plt.ylabel('systolic', weight='bold')
  plt.title('Blood Pressure Classification', weight='bold')

  plt.show(block=block)

def _bp_risk_index_hist(df, block=True):
  """
  Generate a histogram of the risk index of from bp_measurements.

  Args:
    df (DataFrame): The input data as pandas DataFrame.

  Returns:
    histogram: The histogram plot.
   """

  
  #rcParams['font.weight'] = 'bold'
  #plt.rcParams['figure.dpi'] = 150
  #fig, ax = plt.subplots()
  fig = plt.figure()
  ax = fig.add_subplot()
  risk_idx = [ri['idx'] for ri in BPM.risk_classification]
  risk_idx.append(risk_idx[-1]+1) # add right edge of the bins
  #n, bins, patches = ax.hist(df[BPM.risk_index], bins=[x+0.5 for x in risk_idx])
  n, bins, patches = ax.hist(df[BPM.risk_index], bins=risk_idx)

  # center the xticks
  ticks = [patch._x0+0.5 for patch in patches]
  ticklabels = [ri['name'] for ri in BPM.risk_classification]
  plt.xticks(ticks, ticklabels, rotation=60, rotation_mode='anchor', weight='bold', ha='right')
  #ax.tick_params('x', length=5, pad=-10, which='major')
  #ax.set_xticks([])
  #plt.xticks(ticks)
  plt.ylabel('frequency', weight='bold')
  plt.title('Number of Readings per Blood Pressure Classification', weight='bold')
  plt.tight_layout()
  ax.bar_label(patches)
  #ax.bar_label(patches, labels=ticklabels, rotation=60, label_type='edge', padding=-10)
  for i in risk_idx[:-1]:
    patches[i].set_facecolor(category_colors.colors[i])
  """   cmap = ListedColormap(['khaki', 'limegreen', 'green', 'olivedrab', 'gold', 'coral', 'red'])
  ax.imshow(backgr[:-1, :-1], cmap=cmap, alpha=0.5, extent=[X1d[0], X1d[-1], Y1d[0], Y1d[-1]], origin='lower', aspect='auto')

  for i in range(1, len(category_systolic)):
    y = (category_systolic[i] + category_systolic[i-1]) / 2.0 - 2
    plt.annotate(BPM.risk_classification[i-1]['name'], (X1d[0]+2,y))

  plt.xlabel('diastolic', weight='bold')
  plt.ylabel('systolic', weight='bold')
  plt.title('Blood Pressure Classification', weight='bold')
 """
  plt.show(block=block)


def _get_args():
  parser = argparse.ArgumentParser(add_help=False)
  #parser.add_argument(
  #    '-h', '--help', action='help', default=argparse.SUPPRESS, help=text['help_help'][lang]
  #)
  parser.add_argument(
      '-l',
      '--login',
      dest='login',
      required=False,
      action='store_true',
      help='',
  )
  args = parser.parse_args()
  return args


def main():
  args = _get_args()


  df = _read_measurements().reset_index()
  if df is not None:
    print(f'{len(df)} measurements loaded')
    _bp_scatter_plot(df, block=False)
    _bp_risk_index_hist(df)


if __name__ == '__main__':
  main()
