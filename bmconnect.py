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
import base64
import copy
from datetime import date, datetime, timedelta
import hashlib
import beurerbm
from bmconnect_i18n import text_lang, text
from garth.exc import GarthHTTPError
from garminconnect import Garmin, GarminConnectAuthenticationError
from getpass import getpass
import json
import requests
from pathlib import Path

conf_folder = Path.home() / '.config' / 'bmconnect'
conf_file = conf_folder / 'conf.json'
users = {}
default_beurer_user_id = 1
beurer_user_id = default_beurer_user_id
ignore_measurement_user_id = False
lang = 'en'
max_age_days = 90
#max_history_entries = 200
#measurement_history = []
# blood_pressure_rating =


def _login():
  """Login to Garmin Connect, test connection and save credentials on success."""
  garmin = Garmin()
  garmin_email, garmin_password = _get_credentials()
  try:
    garmin = Garmin(garmin_email, garmin_password)
    garmin.login()
    name = garmin.get_full_name()
    print(f'{text["info_login_success_as"][lang]}: {name}')
    users[str(beurer_user_id)] = {'garmin_email': garmin_email, 'garmin_password': garmin_password}
    _write_config()
  except (
      FileNotFoundError,
      GarthHTTPError,
      GarminConnectAuthenticationError,
      requests.exceptions.HTTPError,
  ) as ex:
    print(f'Login error: {ex}')


def _init_garmin_connect():
  """Initialize connection to Garmin Connect with your credentials."""

  try:
    tokenfolder = conf_folder / f'oauth{beurer_user_id}'
    print(f'{text["info_trying_gc_login"][lang]} "{tokenfolder}"...')
    garmin = Garmin()
    garmin.login(tokenfolder)
  except (
      FileNotFoundError,
      GarthHTTPError,
      GarminConnectAuthenticationError,
      requests.exceptions.HTTPError,
  ):
    print(text['info_login_failed_trying_email_pw'][lang])
    try:
      credentials = users.get(str(beurer_user_id))
      print(f'credentials found in config: {credentials}')
      if credentials is None:
        # garmin_email, garmin_password = _get_credentials()
        # Save tokens for next login
        # _write_config()
        print(f'[bmconnect:_init_garmin_connect] Error: {text["error_no_credentials"][lang]}')
        return None
      garmin = Garmin(credentials['garmin_email'], credentials['garmin_password'])
      garmin.login()
      # Save tokens for next login
      garmin.garth.dump(tokenfolder)
    except (
        FileNotFoundError,
        GarthHTTPError,
        GarminConnectAuthenticationError,
        requests.exceptions.HTTPError,
    ):
      return None
  print(text['info_login_success'][lang])
  return garmin


def _get_credentials():
  """Get user credentials from console."""

  email = input(f'{text["info_garmin_email"][lang]}: ')
  password = getpass(f'{text["info_garmin_password"][lang]}: ')
  return email, password


def _read_config():
  global lang
  global users
  global default_beurer_user_id
  #global measurement_history
  print(f'[bmconnect:_read_config] {conf_file}')
  try:
    with conf_file.open() as f:
      config = json.load(f)
      lang = config.get('lang', 'en')
      default_beurer_user_id = config.get('default_beurer_user_id', 1)
      users = config.get('users', {})
      for key in users:
        users[key]['garmin_password'] = base64.b64decode(users[key]['garmin_password']).decode(
            'utf-8'
        )
      #measurement_history = config.get('measurement_history', [])
  except FileNotFoundError:
    # if the file does not exist, it will be created with default values
    pass


def _write_config():
  try:
    # make sure the conf folder exists
    conf_folder.mkdir(parents=True, exist_ok=True)
    with conf_file.open('w') as f:
      json_users = copy.deepcopy(users)  # shallow copy is not enough
      for key in json_users:
        json_users[key]['garmin_password'] = base64.b64encode(
            json_users[key]['garmin_password'].encode('utf-8')
        ).decode('utf-8')
      #json.dump(
      #    {'lang': lang, 'users': json_users, 'measurement_history': measurement_history},
      #    f,
      #)
      json.dump({'lang': lang, 'default_beurer_user_id': default_beurer_user_id, 'users': json_users},f)
  except (PermissionError, IOError, OSError) as e:
    print('[bmconnect:_write_config] Error: ', e)


def _get_all_measurements():
  print(text['info_searching_device'][lang])
  bbm = beurerbm.find()
  if bbm is not None:
    if bbm.connect():
      print(text['info_connected'][lang] + ': ' + bbm.get_name())
      count = bbm.get_count()
      measurements = []
      for i in range(1, count + 1):
        measurements.append(bbm.get_measurement(i))
      bbm.disconnect()
      return measurements
    else:
      print(text['info_could_not_ping_device'][lang])
      bbm.disconnect()
      return None
  else:
    print(text['info_device_not_found'][lang])
    return None


def _get_measurement_hash(measurement: dict) -> str:
  m = measurement.copy()
  # ignore user for hash. The user cannot be retrieved back from Garmin Connect
  m['user']=0
  # ignore calculated fields.
  # They have little to no added value for the hash and are difficult to 
  # retrieved back from Garmin Connect, because we don't know of language settings have changed
  m['irregular heart beat']=False
  m['risk index']=0
  m['recommendation']=''
  return hashlib.sha256(json.dumps(m, sort_keys=True).encode('utf-8')).hexdigest()


def _get_measurement_hashes_from_gc(gc: Garmin, dayspan=max_age_days) -> [str]:
  if not gc:
    return None

  date_end = datetime.today().strftime('%Y-%m-%d')
  date_start = (datetime.today() - timedelta(days=dayspan)).strftime('%Y-%m-%d')
  gc_measurements = gc.get_blood_pressure(date_start, date_end)
  hashes = []
  # extract measurements from garmin structure
  for measurementSummarie in gc_measurements['measurementSummaries']:
    for measurement in measurementSummarie['measurements']:
      m=beurerbm.get_empty_measurement()
      m['systolic']=measurement['systolic']
      m['diastolic']=measurement['diastolic']
      m['pulse rate']=measurement['pulse']
      dt=datetime.fromisoformat(measurement['measurementTimestampLocal'])
      m['day']=dt.day
      m['month']=dt.month
      m['year']=dt.year
      m['hour']=dt.hour
      m['minute']=dt.minute
      m['user']=0
      #ignored by hash, so not worth parsing back
      m['irregular heart beat']=False
      m['risk index']=-1
      m['recommendation']=''
      hashes.append(_get_measurement_hash(m))
  return hashes


def _get_args():
  parser = argparse.ArgumentParser(add_help=False)
  parser.add_argument(
    '-h',
    '--help',
    action='help',
    default=argparse.SUPPRESS,
    help=text['help_help'][lang]
  )
  parser.add_argument(
    '-l',
    '--login',
    dest='login',
    required=False,
    action='store_true',
    help=text['help_login'][lang]
  )
  parser.add_argument(
    '-u',
    '--user',
    dest='user',
    metavar='{1, ..., 255}',
    required=False,
    type=int,
    choices=range(1, 256),
    action='store',
    help=text['help_user'][lang]
  )
  parser.add_argument(
    '-du',
    '--default_user',
    dest='default_user',
    metavar='{1, ..., 255}',
    required=False,
    type=int,
    choices=range(1, 256),
    action='store',
    help=text['help_default_user'][lang]
  )
  parser.add_argument(
    '-i',
    '--ignore',
    dest='ignore_measurement_user_id',
    required=False,
    action='store_true',
    help=text['help_ignore'][lang]
  )
  parser.add_argument(
    '-lc',
    '--language',
    dest='lang',
    required=False,
    type=str.lower,
    choices=text_lang,
    action='store',
    help=text['help_language'][lang]
  )
  args = parser.parse_args()
  return args


def main():
  global default_beurer_user_id
  global beurer_user_id
  global ignore_measurement_user_id
  global lang
  _read_config()
  args = _get_args()

  if args.default_user:
    default_beurer_user_id = args.default_user

  if args.user:
    beurer_user_id = args.user
  else:
    beurer_user_id = default_beurer_user_id

  if args.ignore_measurement_user_id or beurer_user_id not in [1, 2]:
    ignore_measurement_user_id = True

  if args.lang:
    lang = args.lang

  if args.login:
    _login()

  measurements = _get_all_measurements()
  if measurements:
    print(f'{len(measurements)} {text["info_measurements_read"][lang]}')
    gc = _init_garmin_connect()
    # get measurements already uploaded to Garmin Connect
    measurement_history_from_gc = _get_measurement_hashes_from_gc(gc)
    # merge online history with local history
    #measurement_history.extend([m for m in measurement_history_from_gc if m not in measurement_history])
    count = 0
    today = date.today()
    for m in measurements:
      m_date = date(m['year'], m['month'], m['day'])
      if (today - m_date).days > max_age_days:
        # skip this outdated entry
        continue
      m_hash = _get_measurement_hash(m)
      #if m_hash not in measurement_history and (
      if m_hash not in measurement_history_from_gc and (
          ignore_measurement_user_id or m['user'] == 0 or m['user'] == beurer_user_id
      ):
        if not gc:
          gc = _init_garmin_connect()
          if not gc:
            break
        # only work on measurements that are not already uploaded
        timestamp = datetime(
            m['year'], m['month'], m['day'], m['hour'], m['minute'], 0, 0
        ).isoformat()
        notes = ''
        if m['irregular heart beat']:
          notes +=f'{text["arrhythmia recognized"][lang]}\n'
        if m["risk index"] in range(0,7):
          notes += (
            f'{text["info_risk"][lang]}: {m["risk index"]} -'
            f' {text[beurerbm.BeurerBM.risk_classification[m["risk index"]]["id"]][lang]}\n'
          )
        if m["recommendation"]:
          notes += f'{text["Recommendation"][lang]}: {text[m["recommendation"]][lang]}'
        gc.set_blood_pressure(
            m['systolic'], m['diastolic'], m['pulse rate'], timestamp, notes=notes
        )
        #measurement_history.append(m_hash)
        print(f"{timestamp}: {m['systolic']}/{m['diastolic']} {m['pulse rate']}")
        count += 1
    print(f'{count} {text["info_measurements_uploaded"][lang]}')
    #if len(measurement_history) > max_history_entries:
    #  del measurement_history[: len(measurement_history) - max_history_entries]
  _write_config()


if __name__ == '__main__':
  main()
