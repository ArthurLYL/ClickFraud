import pandas as pd
import sys
import pytz
import gc
import time
import os


input_dir = '../input'
work_dir = '../work'

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
train_df = pd.read_csv(input_dir+"/train.csv", dtype=dtypes, usecols=['ip', 'app', 'device', 'os', 'channel', 'click_time', 'is_attributed'], nrows=nrows)
test_df = pd.read_csv(input_dir+"/test.csv", dtype=dtypes, usecols=['ip', 'app', 'device', 'os', 'channel', 'click_time', 'click_id'], nrows=nrows)
test_org_df = pd.read_csv(input_dir+"/test.csv", dtype=dtypes, usecols=['ip', 'app', 'device', 'os', 'channel', 'click_time', 'click_id'], nrows=nrows)
test_df['is_attributed'] = 0

len_train = len(train_df)
df = train_df.append(test_df)


def add_col(df, ptn):
    start = time.time()
    print('start for:', ptn)
    print(df.info())
    name = 'count_' + ptn
    dummy = 'is_attributed'
    cols = ptn.split('_')
    cols_with_dummy = cols.copy()
    cols_with_dummy.append(dummy)
    gp = df[cols_with_dummy].groupby(by=cols)[[dummy]].count().reset_index().rename(index=str, columns={dummy: name})
    _df = df.merge(gp, on=cols, how='left')
    _df[[name]][len_train:].to_csv(work_dir + '/test_' + name + '.csv', index=False)
    _df[[name]][:len_train].to_csv(work_dir + '/train_' + name + '.csv', index=False)
    print('########### done for: ' + name + ' ###########', time.time() - start / 60)
    print(work_dir + '/test_' + name + '.csv')
    print(work_dir + '/train_' + name + '.csv')
    del _df
    gc.collect()


# convert utc to CN time zone
cst = pytz.timezone('Asia/Shanghai')
df['click_time'] = pd.to_datetime(df['click_time']).dt.tz_localize(pytz.utc).dt.tz_convert(cst)
df['hour'] = df['click_time'].dt.hour.astype('uint8')
df['day'] = df.click_time.dt.day.astype('uint8')
test_org_df['click_time'] = pd.to_datetime(test_org_df['click_time']).dt.tz_localize(pytz.utc).dt.tz_convert(cst)
test_org_df['hour'] = test_org_df.click_time.dt.hour.astype('uint8')
test_org_df['day'] = test_org_df.click_time.dt.day.astype('uint8')

# 'ip', 'app', 'device', 'os', 'channel'
patterns = [
    'app_channel',
    'app_device_channel_day_hour',
    'app_device_day_hour',
    'app_os_channel_day_hour',
    'ip_day',
    'ip',
    'ip_app_device_channel_day',
    'ip_app_device_day',
    'ip_app_device_os_day_hour',
    'ip_app_os_channel',
    'ip_app_os_channel_day',
    'ip_os',
]

for ptn in patterns:
    add_col(df, ptn)