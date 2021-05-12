import time
import os
import numpy as np
import pandas as pd
import pytz

# nrows=100000
nrows=None

work_dir = '../work'

name = 'nextClickLeakDay'
newName = 'nextClickLeakDayFlt'
train_df = pd.read_csv(work_dir+"/train_" + name + ".csv", nrows=nrows)
test_df = pd.read_csv(work_dir+"/test_" + name + ".csv", nrows=nrows)
len_train = len(train_df)
df = train_df.append(test_df)

df[newName] = 2
df[newName] -= (df[name] < 1800) & (df[name] > 30)
df[newName] -= (df[name] < 30) * 2

df[[newName]][len_train:].to_csv(work_dir + '/test_' + newName + '.csv', index=False)
print(work_dir + '/test_' + newName + '.csv')
df[[newName]][:len_train].to_csv(work_dir + '/train_' + newName + '.csv', index=False)
print(work_dir + '/train_' + newName + '.csv')
