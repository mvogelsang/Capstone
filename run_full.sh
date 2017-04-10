#!/bin/bash
set -x
cd ./clean_data && rm *.csv
cd ..
rm ./LouData.db
rm ./dbdump.bak
python ./1_CleanData.py
python ./2_LoadDataToDbAndFilter.py
python ./3_BuildModel.py
sqlite3 ./LouData.db .dump > dbdump.bak
