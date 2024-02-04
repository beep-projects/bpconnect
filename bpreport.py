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
from bpm import BPM
from bpconnect_i18n import text_lang, text
from datetime import date, datetime
import json
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.font_manager as fm
import os
import sys

report_folder = Path(os.path.dirname(os.path.abspath(__file__))) / 'report'
sys.path.append(report_folder)
from report.bpreport_template import BpReportTemplate # pylint: disable=wrong-import-position

data_folder = Path.home() / '.bpconnect'
conf_file = data_folder / 'bpreport_conf.json'
data_file = data_folder / 'measurements.feather'
font_folder = report_folder / 'fonts'

lang = 'en'
name = None
birthday = None
gender = None

time_postfix = datetime.now().strftime('%Y%m%d-%H%M%S')

# general plot configuration
### size of figures [width, height] in inches
### DIN A4: 11.6 x 8.2
figsize_full_width = [8, 3.1]
figsize_half_width = [4, 3.1]

### fonts
font_plot_title = {'font': font_folder / 'Roboto-Regular.ttf', 'size': 12, 'wrap': True}
font_plot_ax_label = {'font': font_folder / 'Roboto-Regular.ttf', 'size': 10}
font_plot_ax_ticks = {'font': font_folder / 'Roboto-Regular.ttf', 'size': 8}
font_plot_legend = fm.FontProperties(fname=font_folder / 'Roboto-Regular.ttf', size=8)
### colors
colors_category = [
    (1.0, 1.0, 0.69, 1.0),
    (0.88, 0.95, 0.69, 1.0),
    (0.75, 0.89, 0.46, 1.0),
    (0.57, 0.82, 0.56, 1.0),
    (1.0, 0.94, 0.73, 1.0),
    (1.0, 0.83, 0.71, 1.0),
    (1.0, 0.66, 0.65, 1.0),
    (1.0, 0.55, 0.58, 1.0),
]
color_systolic = 'red'
color_diastolic = 'dodgerblue'
color_pulse_pressure = 'grey'
color_plot_background = (0.75, 0.75, 0.75, 0.25)
### axis ranges
category_systolic = [c['systole min'] for c in BPM.risk_classification]
category_systolic.append(BPM.risk_classification[-1]['systole max'])
category_diastolic = [c['diastole min'] for c in BPM.risk_classification]
category_diastolic.append(BPM.risk_classification[-1]['diastole max'])
# overwrite min and max
category_systolic[0] = 50
category_systolic[-1] = 200
category_diastolic[0] = 20
category_diastolic[-1] = 130


def _read_config():
  global lang
  global name
  global birthday
  global gender
  try:
    with conf_file.open() as f:
      config = json.load(f)
      lang = config.get('lang', 'en')
      name = config.get('name', None)
      bday = config.get('birthday', None)
      if bday:
        birthday = date.fromisoformat(bday)
      gender = config.get('gender', None)
  except FileNotFoundError:
    # if the file does not exist, it will be created with default values
    pass
  except ValueError as e:
    print(f'[bpreport.py:_read_config] Error: {e}')
    pass


def _write_config():
  try:
    # make sure the conf folder exists
    data_folder.mkdir(parents=True, exist_ok=True)
    config = {'lang': lang, 'name': name, 'birthday': None, 'gender': gender}
    if birthday:
      config['birthday'] = birthday.isoformat()
    with conf_file.open('w') as f:
      json.dump(config, f)
  except (PermissionError, IOError, OSError) as e:
    print(f'[bpreport.py:_write_config] Error: {e}')


def _read_measurements():
  try:
    df = pd.read_feather(data_file)
  except FileNotFoundError as e:
    print(f'[bpreport.py:_read_measurements] Error: {e}')
    df = pd.DataFrame()
  if not all(k in list(df.columns) for k in BPM.keys):
    print(f'[bpreport.py:_read_measurements] Error: {data_file} is not a valid measurement file')
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

  x1d = np.arange(category_diastolic[0], category_diastolic[-1], 0.25)
  y1d = np.arange(category_systolic[0], category_systolic[-1], 0.25)
  x_diastole, y_systole = np.meshgrid(x1d, y1d)

  xvals = df[BPM.diastolic].tolist()
  yvals = df[BPM.systolic].tolist()

  backgr = np.full_like(x_diastole, 0)
  for i in range(1, len(BPM.risk_classification)):
    backgr[
        ((x_diastole >= category_diastolic[i]) & (y_systole < category_systolic[i]))
        | ((x_diastole < category_diastolic[i]) & (y_systole >= category_systolic[i]))
        | ((x_diastole >= category_diastolic[i]) & (y_systole >= category_systolic[i]))
    ] = i

  # rcParams['font.weight'] = 'bold'
  # fig, ax = plt.subplots()
  fig = plt.figure(figsize=figsize_full_width)
  # ax = fig.add_subplot()
  # left, bottom, width, height
  ax = fig.add_axes([0.1, 0.15, 0.85, 0.75])

  ax.margins(x=0.2, y=0.2)
  alpha = max(0.1, 20 / len(xvals))
  ax.scatter(xvals, yvals, alpha=alpha, marker='.', s=150, linewidth=0.0, color='black')
  ax.imshow(
      backgr[:-1, :-1],
      cmap=ListedColormap(colors_category),
      extent=[x1d[0], x1d[-1], y1d[0], y1d[-1]],
      origin='lower',
      aspect='auto',
  )

  for i in range(1, len(category_systolic)):
    y = (category_systolic[i] + category_systolic[i - 1]) / 2.0 - 2
    plt.annotate(BPM.risk_classification[i - 1]['name'], (x1d[0] + 2, y), **font_plot_ax_ticks)
  plt.xlabel(text['plot_label_diastolic'][lang], **font_plot_ax_label)
  plt.ylabel(text['plot_label_systolic'][lang], **font_plot_ax_label)
  plt.title(text['plot_title_bp_classification'][lang], **font_plot_title)
  plt.xticks(**font_plot_ax_ticks)
  plt.yticks(**font_plot_ax_ticks)
  # plt.tight_layout()
  plt.show(block=block)
  return fig


def _bp_risk_index_hist(df, block=True):
  """
  Generate a histogram of the risk index of from bp_measurements.

  Args:
    df (DataFrame): The input data as pandas DataFrame.

  Returns:
    histogram: The histogram plot.
  """

  fig = plt.figure(figsize=figsize_half_width)
  ax = fig.add_axes([0.15, 0.40, 0.8, 0.5])

  ax.margins(x=0.2, y=0.2)
  risk_idx = [ri['idx'] for ri in BPM.risk_classification]
  risk_idx.append(risk_idx[-1] + 1)  # add right edge of the bins
  _, _, patches = ax.hist(df[BPM.risk_index], bins=risk_idx)

  # center the xticks
  ticks = [patch._x0 + 0.5 for patch in patches]  # pylint: disable=W0212
  ticklabels = [text[ri['name']][lang] for ri in BPM.risk_classification]
  plt.xticks(
      ticks, ticklabels, rotation=45, rotation_mode='anchor', ha='right', **font_plot_ax_label
  )
  plt.yticks(**font_plot_ax_ticks)
  plt.ylabel(text['plot_label_frequency'][lang], **font_plot_ax_label)
  plt.title(text['plot_title_risk_index_hist'][lang], **font_plot_title)
  ax.bar_label(patches, **font_plot_ax_ticks)
  for i in risk_idx[:-1]:
    patches[i].set_facecolor(colors_category[i])

  ax.set_facecolor(color_plot_background)
  ax.yaxis.grid(which='major', color='white', linewidth=1.0)
  ax.yaxis.grid(which='minor', color='white', linewidth=0.5)
  # Show the minor ticks and grid.
  ax.minorticks_on()
  # force grid lines in the background
  ax.set_axisbelow(True)
  # Now hide the minor ticks (but leave the gridlines).
  ax.tick_params(which='minor', bottom=False)
  ax.tick_params('x', which='major', length=10)

  plt.show(block=block)
  return fig


def _get_cdf(data, interpolate=False):
  """Calc CDF"""
  result = data.value_counts(normalize=True).sort_index().cumsum()
  result = result.reindex(range(result.index.min() - 1, result.index.max() + 1), fill_value=np.nan)
  if interpolate:
    result = result.interpolate()
  result.at[result.index[0]] = 0
  return result.index.to_list(), result.values.tolist()


def _get_pdf(data, interpolate=False):
  x, y = _get_cdf(data, interpolate)
  return (x, np.gradient(y))


def _plot_category_fill(ax, x, y, category):
  start = 0
  last_cat = -1
  for c in range(0, len(category) - 1):
    if category[c] in x:  # and x.index(category[category]):
      stop = x.index(category[c])
      ax.fill_between(
          x[start:stop], y[start:stop], 0, alpha=0.5, color=colors_category[c], linewidth=0.0
      )
      start = stop - 1
      last_cat = c
  # the last category ist never in the array, except there is a serious situation
  ax.fill_between(x[start:], y[start:], 0, alpha=0.5, color=colors_category[last_cat + 1])


def _extend_xy_to_bp_range(x, y):
  x_null = list(
      range(
          min(category_systolic[0], category_diastolic[0]),
          max(category_systolic[-1], category_diastolic[-1]) + 1,
      )
  )
  y_null = [0] * len(x_null)
  x_start = x_null.index(x[0])
  x_end = x_null.index(x[-1]) + 1
  x = x_null
  y = y_null[:x_start] + y + y_null[x_end:]
  return x, y


def _bp_pdfs(df, block=True):
  """
  Generate a histogram of the risk index of from bp_measurements.

  Args:
    df (DataFrame): The input data as pandas DataFrame.

  Returns:
    histogram: The histogram plot.
  """

  fig = plt.figure(figsize=figsize_half_width)
  # left, bottom, width, height
  ax = fig.add_axes([0.15, 0.40, 0.8, 0.5])
  ax.margins(x=0.2, y=0.2)
  syst = df[BPM.systolic]
  x, y = _get_pdf(syst, interpolate=True)
  x, y = _extend_xy_to_bp_range(x, list(y * 100))
  ax.plot(x, y, color_systolic, label=text['plot_label_systolic'][lang])
  _plot_category_fill(ax, x, y, category_systolic)
  diast = df[BPM.diastolic]
  x, y = _get_pdf(diast, interpolate=True)
  x, y = _extend_xy_to_bp_range(x, list(y * 100))
  ax.plot(x, y, color_diastolic, label=text['plot_label_diastolic'][lang])
  _plot_category_fill(ax, x, y, category_diastolic)

  plt.xlabel(text['plot_label_pressure'][lang], **font_plot_ax_label)
  plt.ylabel(text['plot_label_percentage'][lang], **font_plot_ax_label)
  plt.title(text['plot_title_bp_distribution'][lang], **font_plot_title)
  plt.legend(prop=font_plot_legend)

  ax.set_facecolor(color_plot_background)
  ax.grid(which='major', color='white', linewidth=1.0)
  ax.grid(which='minor', color='white', linewidth=0.5)
  # Show the minor ticks and grid.
  ax.minorticks_on()
  # force grid lines in the background
  ax.set_axisbelow(True)
  # Now hide the minor ticks (but leave the gridlines).
  # ax.tick_params(which='minor', bottom=False, left=False)

  plt.xticks(**font_plot_ax_ticks)
  plt.yticks(**font_plot_ax_ticks)
  plt.xlim([min(x), max(x)])
  plt.ylim([min(y), max(y)])

  plt.show(block=block)
  return fig


def _bp_measurement_series(df, block=True):
  # set date as index for grouping
  df = df.set_index('date')
  # add systolic min max avg per day
  df = df.groupby(df.index)[[BPM.systolic, BPM.diastolic, BPM.pulse_pressure]].agg(
      ['min', 'max', 'mean']
  )
  # flatten the GroupBy object
  df.columns = [
      f'{BPM.systolic}_min',
      f'{BPM.systolic}_max',
      f'{BPM.systolic}_mean',
      f'{BPM.diastolic}_min',
      f'{BPM.diastolic}_max',
      f'{BPM.diastolic}_mean',
      f'{BPM.pulse_pressure}_min',
      f'{BPM.pulse_pressure}_max',
      f'{BPM.pulse_pressure}_mean',
  ]
  df = df.reset_index()
  # add risk_index column for daily averages
  df['risk_index'] = [
      BPM.get_risk_assessment(row[f'{BPM.systolic}_mean'], row[f'{BPM.diastolic}_mean'])[0]
      for index, row in df.iterrows()
  ]
  # create figure
  fig = plt.figure(figsize=figsize_full_width)
  ax = fig.add_axes([0.1, 0.15, 0.85, 0.75])
  ax.plot(
      df[BPM.date],
      df[f'{BPM.systolic}_mean'],
      color=color_systolic,
      label=text['plot_label_systolic'][lang],
      zorder=3,
  )
  ax.fill_between(
      df[BPM.date],
      df[f'{BPM.systolic}_min'],
      df[f'{BPM.systolic}_max'],
      color=color_systolic,
      alpha=0.15,
      zorder=2,
  )
  ax.plot(
      df[BPM.date],
      df[f'{BPM.diastolic}_mean'],
      color=color_diastolic,
      label=text['plot_label_diastolic'][lang],
      zorder=3,
  )
  ax.fill_between(
      df[BPM.date],
      df[f'{BPM.diastolic}_min'],
      df[f'{BPM.diastolic}_max'],
      color=color_diastolic,
      alpha=0.15,
      zorder=2,
  )
  # add markers with category colors
  for risk_index in range(0, len(colors_category)):
    dates = df[df['risk_index'] == risk_index][BPM.date]
    systolic_mean = df[df['risk_index'] == risk_index][f'{BPM.systolic}_mean']
    diastolic_mean = df[df['risk_index'] == risk_index][f'{BPM.diastolic}_mean']
    ax.plot(
        dates,
        systolic_mean,
        linestyle='None',
        marker='.',
        markersize=10,
        color=colors_category[risk_index],
        zorder=4,
    )
    ax.plot(
        dates,
        diastolic_mean,
        linestyle='None',
        marker='.',
        markersize=10,
        color=colors_category[risk_index],
        zorder=4,
    )
    ax.plot(
        (dates, dates),
        (systolic_mean, diastolic_mean),
        linewidth=5,
        color=colors_category[risk_index],
        alpha=0.5,
        zorder=1,
    )

  ax.plot(
      df[BPM.date],
      df[f'{BPM.pulse_pressure}_mean'],
      color=color_pulse_pressure,
      label=text['plot_label_pulse_pressure'][lang],
      zorder=3,
  )
  ax.fill_between(
      df[BPM.date],
      df[f'{BPM.pulse_pressure}_min'],
      df[f'{BPM.pulse_pressure}_max'],
      color=color_pulse_pressure,
      alpha=0.15,
      zorder=2,
  )

  # set title and labels
  plt.xlabel(text['plot_label_date'][lang], **font_plot_ax_label)
  plt.ylabel(text['plot_label_pressure'][lang], **font_plot_ax_label)
  plt.title(text['plot_title_bp_measurement_series'][lang], **font_plot_title)
  plt.legend(prop=font_plot_legend)
  # set grid
  ax.set_facecolor(color_plot_background)
  ax.grid(which='major', color='white', linewidth=1.0)
  ax.grid(which='minor', color='white', linewidth=0.5)
  # Show the minor ticks and grid.
  ax.minorticks_on()
  # force grid lines in the background
  ax.set_axisbelow(True)
  # Now hide the minor ticks (but leave the gridlines).
  # ax.tick_params(which='minor', bottom=False, left=False)

  plt.xticks(**font_plot_ax_ticks)
  plt.yticks(**font_plot_ax_ticks)
  plt.xlim([min(df[BPM.date]), max(df[BPM.date])])
  plt.ylim([category_diastolic[0], category_systolic[-1]])
  plt.show(block=block)
  return fig


def _save_fig(fig, path, img_type='svg', dpi=300):
  fig.savefig(path, format=img_type, dpi=dpi)


def _get_args():
  parser = argparse.ArgumentParser()  # add_help=False)
  parser.add_argument(
      '-n',
      '--name',
      dest='name',
      required=False,
      type=str,
      action='store',
      help=text['help_name'][lang],
  )
  parser.add_argument(
      '-b',
      '--birthday',
      dest='birthday',
      required=False,
      type=str,
      action='store',
      help=text['help_birthday'][lang],
  )
  parser.add_argument(
      '-sd',
      '--start_date',
      dest='start_date',
      required=False,
      type=str,
      action='store',
      help=text['help_start_date'][lang],
  )
  parser.add_argument(
      '-ed',
      '--end_date',
      dest='end_date',
      required=False,
      type=str,
      action='store',
      help=text['help_end_date'][lang],
  )
  parser.add_argument(
      '-g',
      '--gender',
      dest='gender',
      required=False,
      type=str,
      action='store',
      help=text['help_gender'][lang],
  )
  parser.add_argument(
      '-lc',
      '--language',
      dest='lang',
      required=False,
      type=str.lower,
      choices=text_lang,
      action='store',
      help=text['help_language'][lang],
  )

  args = parser.parse_args()
  return args


def main():
  global lang
  global name
  global birthday
  global gender

  start_date = None
  end_date = None

  _read_config()

  args = _get_args()
  config_changed = False
  if args.name:
    name = args.name
    config_changed = True

  if args.birthday:
    birthday = date.fromisoformat(args.birthday)
    config_changed = True

  if args.gender:
    gender = args.gender
    config_changed = True

  if args.lang:
    lang = args.lang
    config_changed = True

  if args.start_date:
    start_date = datetime.fromisoformat(args.start_date).date()

  if args.end_date:
    end_date = datetime.fromisoformat(args.end_date).date()

  if config_changed:
    _write_config()

  df = _read_measurements().reset_index(drop=True)
  if df is not None:
    # drop unwanted measurements
    if start_date:
      df = df.drop(df[(df[BPM.date] < start_date)].index)
    if end_date:
      df = df.drop(df[(df[BPM.date] > end_date)].index)

    print(f'[bpreport.py:main] {len(df)} measurements loaded')
    fig_measurement_series = _bp_measurement_series(df, block=False)
    _save_fig(fig_measurement_series, (report_folder / 'measurement_series.svg'))

    fig_scatter = _bp_scatter_plot(df, block=False)
    _save_fig(fig_scatter, (report_folder / 'scatter.svg'))

    fig_hist = _bp_risk_index_hist(df, block=False)
    _save_fig(fig_hist, (report_folder / 'hist.svg'))

    fig_pdfs = _bp_pdfs(df, block=False)
    _save_fig(fig_pdfs, (report_folder / 'pdfs.svg'))

    report = BpReportTemplate(report_folder, 'bpreport_template.html')
    report.set_name(name)
    report.set_birthday_gender(birthday, gender)
    report.set_data(df)
    report.translate_template(text, lang)
    report.save_as_pdf(report_folder / f'bpreport_{time_postfix}.pdf')


if __name__ == '__main__':
  main()
