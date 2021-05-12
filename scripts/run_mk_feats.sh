#!/bin/sh

mkdir -p /home/lyl/4thPlace/work
#mkdir -p ../csv
path=/home/lyl/4thPlace/mk_feat
# make mapping click_id
#python $path/mk_mapping.py

# basic features
#python $path/mk_feat_base.py

# couting features
#python $path/counting/mk_feat_count.py
#python $path/counting/mk_feat_count_time.py
#python $path/counting/mk_feat_countRatio.py

# cumulative count
#python $path/cumulative/mk_feat_cumcount.py
#python $path/cumulative/mk_feat_recumcount.py
#python $path/cumulative/mk_feat_cumratio.py

#time to next click with leak
#python $path/nextClick/mk_feat_nextClick_leak_day.py
#python $path/nextClick/mk_feat_nextClick_filter.py

# time bucket count.(make multiple time intervals, and count the bucket count wich the IP exists)
#python $path/timeBucket/mk_feat_rangecount.py
#python $path/timeBucket/mk_feat_rangecount_minute.py

# variance
#python $path/mk_feat_var.py

# common IP
#python $path/mk_feat_common_ip.py

# unique count
#python $path/mk_feat_uniq_count2.py

# whole
python $path/mk_feat_woe_bound.py
python -u ./main.py  model=LGBM_feat=lgbmBest_categoricalThreVal=10000_validation=subm_params=-,gbdt,0.45,0.04,188,7,auc,20,5,0,20,76,binary,0,0,32.0,1.0,200000,1,0 > /tmp/lgbm.log 2>&1; grep "validation auc:" /tmp/lgbm.log
#python ./main.py BatchNormalization=on_sameNDenseAsEmb=off_model=keras_feat=kerasBest_validation=team_params=-,20000,1000,1,0.2,100,2,0.001,0.0001,0.001,100,2,3 > /tmp/keras.log 2>&1; grep "validation auc:" /tmp/keras.log