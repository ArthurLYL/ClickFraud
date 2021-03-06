import pandas as pd
import sys
import pytz
import gc
import time

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

# nrows = 100000
nrows = None
train_df = pd.read_csv(input_dir+"/train.csv", dtype=dtypes, usecols=['ip', 'app', 'device', 'os', 'channel', 'click_time', 'is_attributed'], nrows=nrows)
test_df = pd.read_csv(input_dir+"/test.csv", dtype=dtypes, usecols=['ip', 'app', 'device', 'os', 'channel', 'click_time', 'click_id'], nrows=nrows)
test_org_df = pd.read_csv(input_dir+"/test.csv", dtype=dtypes, usecols=['ip', 'app', 'device', 'os', 'channel', 'click_time', 'click_id'], nrows=nrows)
test_df['is_attributed'] = 0

len_train = len(train_df)
df = train_df.append(test_df)
df["machine"] = 1000*df["device"] + df["os"]
cst = pytz.timezone('Asia/Shanghai')
df['click_time'] = pd.to_datetime(df['click_time']).dt.tz_localize(pytz.utc).dt.tz_convert(cst)
df['hour'] = df.click_time.dt.hour.astype('uint8')
df['day'] = df.click_time.dt.day.astype('uint8')


def add_col(df, ptn):
    start = time.time()
    print('start for:',ptn)
    name = "uniqueCount_" + ptn
    cols = ptn.split("_")
    gp = df[cols].groupby(by=cols[0:len(cols)-1])[cols[len(cols)-1]].nunique().reset_index().rename(index=str, columns={cols[len(cols)-1]: name})
    _df = df.merge(gp, on=cols[0:len(cols)-1], how='left')
    _df[[name]][len_train:].to_csv(work_dir + '/test_' + name + '.csv', index=False)
    _df[[name]][:len_train].to_csv(work_dir + '/train_' + name + '.csv', index=False)
    print('########### done for: ' + name + ' ###########', time.time()-start/60)
    print(work_dir + '/test_' + name + '.csv')
    print(work_dir + '/train_' + name + '.csv')

    name_ratio = "uniqueCountRatio_" + ptn
    dummy = 'is_attributed'
    cols = cols[0:len(cols)-1]
    cols_with_dummy = cols.copy()
    cols_with_dummy.append(dummy)
    gp = df[cols_with_dummy].groupby(by=cols)[[dummy]].count().reset_index().rename(index=str, columns={dummy: name_ratio})
    _df_ratio = df.merge(gp, on=cols, how='left')
    _df_ratio[name_ratio] = _df[name] / _df_ratio[name_ratio]
    _df_ratio[[name_ratio]][len_train:].to_csv(work_dir + '/test_' + name_ratio + '.csv', index=False)
    _df_ratio[[name_ratio]][:len_train].to_csv(work_dir + '/train_' + name_ratio + '.csv', index=False)
    print('########### done for: ' + name_ratio + ' ###########', time.time()-start/60)
    print(work_dir + '/test_' + name_ratio + '.csv')
    print(work_dir + '/train_' + name_ratio + '.csv')
    del _df
    del _df_ratio
    gc.collect()


patterns = [
    'day_ip_machine',
    'day_ip_os',
    'day_ip_device',
    'day_ip_app',
    'day_ip_channel',
    'machine_app',
    'machine_channel',
    'machine_ip',
]

for ptn in patterns:
    add_col(df, ptn)