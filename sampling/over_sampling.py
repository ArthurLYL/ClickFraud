from imblearn.over_sampling import RandomOverSampler, SMOTE
import pandas as pd
import pytz
import matplotlib.pyplot as plt

input_dir = "../input"
work_dir = "../work"
cols = ['ip', 'app', 'device', 'os', 'channel', 'hour', 'day', 'is_attributed']


def handle(train_df):
    X = train_df.iloc[:, lambda x: x.columns != 'is_attributed'].to_numpy()
    y = train_df.is_attributed.to_numpy()


# def over_sampling():
#     # Over_Sampling
#     ros = RandomOverSampler()
#     X_ros, y_ros = ros.fit_sample(X, y)
#
#     DataAll = pd.DataFrame(X_ros, columns=cols[:-1])
#     DataAll['is_attributed'] = y_ros
#     DataAll.to_csv(work_dir + "/rostrain.csv", index=False)


def smote_sampling(X, y):
    # SMOTE_Sampling
    smote = SMOTE(random_state=2021)
    X_smote, y_smote = smote.fit_resample(X, y)

    DataAll = pd.DataFrame(X_smote, columns=cols[:-1])
    DataAll['is_attributed'] = y_smote
    return DataAll
