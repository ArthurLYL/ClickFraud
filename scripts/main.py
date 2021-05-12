import pandas as pd
import model_lib
from lib_util import get_target, get_opt
from read_data import read_data_ph1, read_csv
import datetime

target = get_target()
start = datetime.datetime.now()
print('Start time is: ', start)
print('start for', target)

train_df, test_df, numerical_patterns, cat_patterns = read_data_ph1()
print('Reading data over')
predictors = numerical_patterns + cat_patterns
categorical = cat_patterns

is_val = (train_df['day'] == 9) & ((train_df['hour'] == 13) | (train_df['hour'] == 17) | (train_df['hour'] == 21))
val_df = train_df[is_val]
train_df = train_df[~is_val]
print('Start to predict')
auc = model_lib.Predict(train_df, val_df, test_df, predictors, categorical, seed=get_opt('seed',2020))
print('validation auc:', auc)

test_df = test_df[['pred']].rename(columns={'pred': 'is_attributed'})
test_df['click_id'] = test_df.index
# mapping = read_csv('../input/mapping.csv')
# test_df = test_df.merge(mapping, on='click_id', how='inner')
"""
# original code
click_id = read_csv('../input/sample_submission.csv', usecols=['click_id'])
test_df = test_df.reset_index().merge(mapping, left_on='index', right_on='old_click_id', how='left')
test_df = click_id.merge(test_df, on='click_id', how='left')
"""
outfile = '../csv/pred_test_'+target+'.csv'
print('writing to', outfile)
test_df[['click_id', 'is_attributed']].to_csv(outfile, index=False)
end = datetime.datetime.now()
print('End time is: ', end)
print('Running time is: ', end-start)