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

## Process of big data sets

1. When reading .csv using Pandas, using the appropriate data types (uint8, uint16, uint32, float32, etc.) and assigning values to parameters `usecols` and `dtypes`.  Otherwise it will use uint64 to read non-negative integers, use float64 to read floating-point numbers and integers with some null values.
2. Many variables are just used or twice, when a variable `a` (especially a large memory variable) is no longer used, remove it from memory: `del a`.
3. We often use a variable to refer to different objects. At the same time, we will generate some objects that can no longer be referred. In theory, Python will automatically do garbage collection, but we need to trigger manually sometimes. We can often call the function `gc.collect()` to trigger garbage collection.
4. We usually perform one-hot encoding for categorical features to ensure the model not to treat them as  ordered continuous values. But the feature dimension will be extremely large after encoding, leading to large memory consumption. LightGBM optimizes the categorical features and only needs to specify the categorical features when preparing the dataset for model.

## Reference

https://zhuanlan.zhihu.com/p/36852456

https://www.kaggle.com/anttip/talkingdata-wordbatch-fm-ftrl-lb-0-9769/data (mapping)

https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection/discussion/56475#328145

https://github.com/ShawnyXiao/2018-Kaggle-AdTrackingFraud

https://www.kaggle.com/alexfir/mapping-between-test-supplement-csv-and-test-csv/data?select=mapping.csv (mapping)

https://www.kaggle.com/c/talkingdata-adtracking-fraud-detection/discussion/56545