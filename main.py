import pandas as pd
import sys
import pytz
import gc
import time
import os
import numpy as np

input_dir = './input'
work_dir = './work'

dtypes = {
    'ip': 'uint32',
    'app': 'uint16',
    'device': 'uint16',
    'os': 'uint16',
    'channel': 'uint16',
    'is_attributed': 'uint8',
    'click_id': 'uint32'
}

# nrows = 10000
nrows = None
cst = pytz.timezone('Asia/Shanghai')
df = pd.read_csv(input_dir + "/train.csv", dtype=dtypes,
                 usecols=['ip', 'app', 'device', 'os', 'channel', 'click_time', 'is_attributed'], nrows=nrows)
df['click_time'] = pd.to_datetime(df['click_time'])
print(9308568+68941878+131886953+184903890+184903890)
print(len(df))
# print(len(df[df['click_time'] < np.datetime64('2017-11-07 00:00:00')]))
# print(len(df[df['click_time'] < np.datetime64('2017-11-08 00:00:00')]))
# print(len(df[df['click_time'] < np.datetime64('2017-11-09 00:00:00')]))
# print(len(df[df['click_time'] < np.datetime64('2017-11-10 00:00:00')]))
# print(len(df[df['click_time'] < np.datetime64('2017-11-11 00:00:00')]))

