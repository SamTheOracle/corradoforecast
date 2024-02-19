import os
import csv
from datetime import datetime as dt
from io import StringIO

class FormTuple:
    def __init__(self, key, value):
        self.form_key = key
        self.form_value = value
    def __str__(self) -> str:
        return f"{self.form_key}->{self.form_value}"
    def __repr__(self):
        return f"{self.form_key}->{self.form_value}"


def compute_forecast(input:list[FormTuple]):
   csv_filter = filter(lambda input_filter: input_filter.form_key==os.getenv("FORM_FILE_KEY"), input)
   reader = csv.reader(StringIO(list[FormTuple](csv_filter)[0].form_value.decode()))
   filename = f"output-{dt.utcnow()}.csv"
   with open(filename, mode='xt') as csv_output:
    writer = csv.writer(csv_output)
    for row in reader:
        writer.writerow(row)
   return open(filename, 'rt').read()    