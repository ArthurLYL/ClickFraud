import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

input_dir = "../input"
work_dir = "../work"
dtypes = dtypes = {
    'ip': 'uint32',
    'app': 'uint16',
    'device': 'uint16',
    'os': 'uint16',
    'channel': 'uint16',
    'is_attributed': 'uint8',
    'click_id': 'uint32'
}
train_df = pd.read_csv(input_dir + "/train.csv", dtype=dtypes, usecols=['ip', 'app', 'device', 'os', 'channel', 'click_time', 'is_attributed'], nrows=None)
count = train_df['is_attributed'].value_counts()
count.plot(kind='barh', title='is_attributed(Count')
plt.show()
