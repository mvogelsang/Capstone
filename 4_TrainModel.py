import subprocess
import os
import sqlite3
import datetime
import sqlQueries
import sklearn
from sklearn import preprocessing
import pyglmnet
import numpy
import math
import pickle
import sklearn.metrics as skm

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

def getglmnet():
    return pyglmnet.GLM(distr='gaussian', alpha=0.05, score_metric='pseudo_R2')

def getStandardScaler(trainingInput):
    scaler = preprocessing.StandardScaler()
    scaler.fit(trainingInput)
    return scaler

def getTestPredictions(testInput, analysisTool):
    predictions = []
    for sample in testInput:
        prediction = analysisTool.predict(sample)
        prediction = numpy.mean(prediction)
        predictions.append(prediction)

    return predictions

def fitEstimator(tool, )
def main():

    # get the necessary components to build and use an analysis tool
    print( 'getting input...')
    tInput = getModelTrainingInput()
    print( 'getting output...')
    tOutput = getModelTrainingOutput()
    if len(tInput) != len(tOutput):
        print( 'WARNING training input/output mismatch')

    # get scaler and standardize the input data
    print( 'scaling...')
    scaler = getStandardScaler(tInput)
    tInput = scaler.transform(tInput)

    # get a test input and output set
    print( 'creating data subsets..')
    prelimInput = tInput[0:-5000]
    prelimOutput = tOutput[0:-5000]
    testInput = tInput[-5000: -1]
    testOutput = tOutput[-5000: -1]

    # get the tools
    print( 'getting tools...')
    glmnet = getglmnet()
    ardRegressor =


    # train the models
    print( 'training glm...')
    glmnet.fit(prelimInput,prelimOutput)
    print( 'training ard...')
    ardRegressor.fit(prelimInput, tOutput)

    # get initial measure of performance
    print( 'R^2 Scores')
    print( 'glmnet - ' + str(skm.r2_score(testOutput, getTestPredictions(testInput, glmnet))))
    print( 'glmnet - ' + str(skm.r2_score(testOutput, getTestPredictions(testInput, ardRegressor))))


    # # save the input scaler and the model for later use
    # print( 'saving scaler and model...')
    # with open("./pickles/scaler.pickle", "wb") as output_file:
    #     pickle.dump(scaler, output_file)
    # with open("./pickles/glmnet.pickle", "wb") as output_file:
    #     pickle.dump(glmnet, output_file)


    dbConn.commit()
    dbConn.close()

if __name__ == "__main__":
    main()
