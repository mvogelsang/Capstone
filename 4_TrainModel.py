import subprocess
import os
import sqlite3
import datetime
import sqlQueries
from sklearn import preprocessing
import pyglmnet
import numpy
import math
import pickle

# note, for convenience of writing many separate query functions
# the connection is defined globally
dbConn = sqlite3.connect("./LouData.db", detect_types=sqlite3.PARSE_DECLTYPES);
# dbConn.row_factory = sqlite3.Row
dbCursor = dbConn.cursor()
dbCursor.executescript(sqlQueries.E_speedConfigure_0)

def getModelTrainingInput():
    dbCursor.execute(sqlQueries.G_modelTrainingInput_0)
    data = dbCursor.fetchall()
    return numpy.array(data)

def getModelTrainingOutput():
    dbCursor.execute(sqlQueries.G_modelTrainingOutput_0)
    temp = dbCursor.fetchall()

    # flatten the list of tuples received
    flattened = list(sum(temp, ()))
    return numpy.array(flattened)

def getAnalyzer():
    return pyglmnet.GLM(distr='gaussian', alpha=0.05, score_metric='pseudo_R2')

def getStandardScaler(trainingInput):
    scaler = preprocessing.StandardScaler()
    scaler.fit(trainingInput)
    return scaler

def main():
    # get the necessary components to build and use an analysis tool
    print 'getting input...'
    tInput = getModelTrainingInput()
    print 'getting output...'
    tOutput = getModelTrainingOutput()
    if len(tInput) != len(tOutput):
        print 'WARNING training input/output mismatch'
    print 'getting analyzer...'
    analyzer = getAnalyzer()
    scaler = getStandardScaler(tInput)

    # standardize the input data
    tInput = scaler.transform(tInput)

    # train the model
    print 'training model...'
    analyzer.fit(tInput,tOutput)

    # save the input scaler and the model for later use
    print 'saving scaler and model...'
    with open("./scaler.pickle", "wb") as output_file:
        pickle.dump(scaler, output_file)
    with open("./analyzer.pickle", "wb") as output_file:
        pickle.dump(analyzer, output_file)


    dbConn.commit()
    dbConn.close()

if __name__ == "__main__":
    main()
