#!/bin/bash
set -x
cd ./clean_data && rm *.csv
cd ..
. ./bin/activate
rm ./LouData.db
rm ./dbdump.bak
python ./1_CleanData.py
python ./2_LoadDataToDbAndFilter.py
sqlite3 ./LouData.db .dump > dbdump.bak
python ./3_BuildModel.py && sqlite3 ./LouData.db .dump > dbdump.bak
python ./4_TrainModel.py
python ./testModelPerformance.py
set +x
