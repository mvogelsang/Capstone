#!/bin/bash
. ./venv/bin/activate

set -x
cd ./clean_data && rm *.csv && cd ..
rm ./LouData.db
rm ./dbdump.bak
cd ./bimonthlyCharts && rm *.png && cd ..
python ./1_CleanData.py
python ./2_LoadDataToDbAndFilter.py
sqlite3 ./LouData.db .dump > dbdump.bak
python ./3_BuildModel.py && sqlite3 ./LouData.db .dump > dbdump.bak
python ./4_TrainModel.py
python ./testModelPerformance.py
set +x

deactivate
