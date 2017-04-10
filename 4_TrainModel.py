import subprocess
import os
import sqlite3
import datetime
import sqlQueries
from sklearn import preprocessing
import pyglmnet
import numpy
import math

# note, for convenience of writing many separate query functions
# the connection is defined globally
dbConn = sqlite3.connect("./LouData.db", detect_types=sqlite3.PARSE_DECLTYPES);
# dbConn.row_factory = sqlite3.Row
dbCursor = dbConn.cursor()
dbCursor.executescript(sqlQueries.E_speedConfigure_0)

def getModelTrainingInput():
    dbCursor.execute(sqlQueries.G_modelTrainingInput_0)
    scaled = preprocessing.scale(dbCursor.fetchall())
    return numpy.array(scaled)

def getModelTrainingOutput():
    dbCursor.execute(sqlQueries.G_modelTrainingOutput_0)
    temp = dbCursor.fetchall()

    # flatten the list of tuples received
    flattened = list(sum(temp, ()))
    return numpy.array(flattened)

def getAnalysisTool():
    return pyglmnet.GLM(distr='gaussian', alpha=0.05, score_metric='pseudo_R2')

def testAnalyzer(tInput, tOutput, analyzer):
    print 'fitting'
    analyzer.fit(tInput[10:8000],tOutput[10:8000])
    print 'scoring'
    score = analyzer.score(tInput[0:1000],tOutput[0:1000])
    print score
    print 'ten'
    score = analyzer.score(tInput[0:10],tOutput[0:10])
    print score
    print 'prediction'
    p = analyzer[0].predict(tInput[0:1000])
    l = []
    for i,d in enumerate(p):
        l.append(abs(d - tOutput[i]))
    print min(l)
    print max(l)
    print numpy.mean(l)
    return

def getPredictiveInput():
    return

def analyzeCurrentRestarauntModels(predictionInput, analyzer):
    return

def outputSchedule(inspectionSchedule):
    return

def main():
    # get the necessary components to build and use an analysis tool
    print 'getting input...'
    tInput = getModelTrainingInput()
    print 'getting output...'
    tOutput = getModelTrainingOutput()
    if len(tInput) != len(tOutput):
        print 'WARNING training input/output mismatch'
    analyzer = getAnalysisTool()

    # test the analysis tool (not used once usefulness is confirmed)
    # this function simply checked to see if the analyzer was
    # reacting meaningfully to different inputs
    testAnalyzer(tInput, tOutput, analyzer)

    # get the most up-to-date information for each restaraunt
    # predict the score of their next inspection
    # and sort them accordingly
    predictionInput = getPredictiveInput()
    inspectionSchedule = analyzeCurrentRestarauntModels(predictionInput, analyzer)
    outputSchedule(inspectionSchedule)

    dbConn.commit()
    dbConn.close()

if __name__ == "__main__":
    main()
