# -*- coding: utf-8 -*-
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

"""Module used by bpreport.py, which provides class BpReportTemplate"""


import xhtml2pdf.pisa as pisa
from datetime import date, datetime
from pathlib import Path
import sys
sys.path.append(Path(__file__).parent.parent.resolve())
from bpm import BPM



class BpReportTemplate:
  """Helper class for bpreport.py to manage the handling/filling of the report template"""

  template_folder = Path('.')
  template_file = 'bpreport_template.html'
  html = None

  def __init__(self, template_folder, template_file):
    self.template_folder = Path(template_folder)
    self.template_file = template_file
    print(f'[bpreport_template.py:__init__] using template file: {self.template_folder / template_file}')
    with open(self.template_folder / self.template_file, 'r', encoding='utf-8') as f:
      self.html = f.read()

  def set_name(self, name):
    if not name:
      name = ''
    self.html = self.html.replace('[NAME]', name)

  def set_birthday_gender(self, birthday=None, gender=None):
    birthday_age_gender = ''
    if birthday and isinstance(birthday, date):
      today = date.today()
      age = today.year - birthday.year - ((today.month, today.day) < (birthday.month, birthday.day))
      birthday_age_gender = f'{birthday.strftime("%-d. %b %Y")} ( {age} [ABBREV_YEARS] )'
    if gender:
      if birthday_age_gender:
        birthday_age_gender += f' • {gender}'
      else:
        birthday_age_gender = gender
    self.html = self.html.replace('[BIRTHDAYAGEGENDER]', birthday_age_gender)

  def set_dates(self, start_date, end_date=None):
    date_string = start_date.strftime('%-d. %b %Y')
    if end_date:
      date_string += ' - ' + end_date.strftime('%-d. %b %Y')
    self.html = self.html.replace('[STARTDATE-ENDDATE]', date_string)
    self.html = self.html.replace('[DATE]', date.today().strftime('%-d. %b %Y'))

  def set_data(self, df):
    # sort data by date
    df = df.sort_values([BPM.date, BPM.time], ascending=False)
    start_date = df.iloc[-1][BPM.date]
    end_date = df.iloc[0][BPM.date]
    self.set_dates(start_date, end_date)

    rows_html = ''
    for _, row in df.iterrows():
      notes = ''
      if row[BPM.irregular_heart_beat]:
        notes += '<span class="red_heart">&#9829;</span> Arrythmia recognized!<br/>'
      if row[BPM.recommendation]:
        notes += f'{row[BPM.recommendation]}'
      rows_html += (
          '<tr class="readings">\n'
          f'<td class="readings">{datetime.combine(row[BPM.date], row[BPM.time]).strftime("%x %X")}</td>\n'
          f'<td class="readings">{row[BPM.systolic]} / {row[BPM.diastolic]}</td>\n'
          f'<td class="readings">{row[BPM.pulse_pressure]}</td>\n'
          f'<td class="readings">{row[BPM.pulse]}</td>\n'
          f'<td class="readings">{row[BPM.risk_index]} - {BPM.risk_classification[row[BPM.risk_index]]["name"]}</td>\n'
          f'<td class="readings">{notes}</td>\n'
          '</tr>\n'
      )
    self.html = self.html.replace('[MEASUREMENTDATA]', rows_html)
    return None

  def translate_template(self, text, lang):
    
    for key in text:
      self.html = self.html.replace(text[key]['en'], text[key][lang])

    self.html = self.html.replace('[META_CONTENT]', text['template_meta_content'][lang])
    self.html = self.html.replace('[DOCUMENT_TITLE]', text['template_document_title'][lang])
    self.html = self.html.replace('[DISCLAIMER]', text['template_disclaimer'][lang])
    self.html = self.html.replace('[ABBREV_YEARS]', text['template_abbrev_years'][lang])
    self.html = self.html.replace(
        '[SECTION_TITLE_MEASUREMENTS]', text['template_section_title_measurements'][lang]
    )
    self.html = self.html.replace('[TABLE_HEADER_TIME]', text['template_table_header_time'][lang])
    self.html = self.html.replace(
        '[TABLE_HEADER_MEASUREMENT]', text['template_table_header_measurement'][lang]
    )
    self.html = self.html.replace('[TABLE_HEADER_PULSE_PRESSURE]', text['template_table_header_pulse_pressure'][lang])
    self.html = self.html.replace('[TABLE_HEADER_PULSE]', text['template_table_header_pulse'][lang])
    self.html = self.html.replace(
        '[TABLE_HEADER_CLASSIFICATION]', text['template_table_header_classification'][lang]
    )
    self.html = self.html.replace('[TABLE_HEADER_NOTES]', text['template_table_header_notes'][lang])
    self.html = self.html.replace(
        '[DOCUMENT_FOOTER_DATE]', text['template_document_footer_date'][lang]
    )

  def save_as_pdf(self, filepath):
    pdf_file = open(filepath, 'w+b')
    pisa.log.setLevel('WARNING')  # suppress debug log output
    pisa.CreatePDF(
        self.html,
        dest=pdf_file,
        encoding='utf-8',
        path=f'{self.template_folder / self.template_file}'
    )
    print(f'[bpreport_template.py:saveAsPDF] PDF saved to: {filepath}')

    pdf_file.close()
