# Passive Detection: Machine Learning Part

## Data sets source and Models

Data sets  is from 'TalkingData AdTracking Fraud Detection Challenge' in Kaggle (**https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection**).

Model definition can be found in [scripts/model_lib.py](./scripts/model_lib.py)

  - **model1** LGBM with 83 (76 numerical, 7 categorical) features.
  - **model2** Keras with 27 (18 numerical, 7 categorical) features.
## Feature Engineering and scripts
Most of these features have already been discussed on the Kaggle forum.
 - counting features
     - mk_feat_count_py
     - mk_feat_count_time.py
     - mk_feat_countRatio.py
 - cumulative count
     - mk_feat_cumcount.py
     - mk_feat_recumcount.py
     - mk_feat_cumratio.py
- time to next click
  - mk_feat_nextClick_leak_day.py
  - mk_feat_nextClick_filter.py
- time bucket count (make multiple time intervals, and count the number of buckets which the IP exists)
  - mk_feat_rangecount.py
  - mk_feat_rangecount_minute.py
- variance
  - mk_feat_var.py
- common IP
  - mk_feat_common_ip.py
- unique count
  - mk_feat_uniq_count2.py
- target encoding: woe
  - mk_feat_woe_bound.py

Features will be calculated once and then saved to disk.

Importance from LGBM is listed in [importance.txt](./importance.txt)

## About running

Put sample_submission.csv, test.csv, test_supplement.csv, train.csv to 'input' directory.

Output prediction files will be in 'csv' directory.

Model1 requires large memory, model2 requires GPU.



