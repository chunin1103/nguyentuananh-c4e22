import pyexcel
from collections import OrderedDict


data = [
    OrderedDict({
        'Name': 'Tuan',
        'Age': 32
    }),
    OrderedDict({
        'Name': 'Afer',
        'Age': 20
    }),
    OrderedDict({
        'Name': 'Rerer',
        'Age': 2
    }),
    OrderedDict({
        'Name': 'Err',
        'Age': 220
    }),
]

pyexcel.save_as(records = data, dest_file_name = "sample.xlsx")