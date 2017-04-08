import subprocess
import os
import sqlite3
import datetime

# note, for convenience of writing many separate query functions
# the connection is defined globally
dbConn = sqlite3.connect("./LouData.db", detect_types=sqlite3.PARSE_DECLTYPES);
dbConn.row_factory = sqlite3.Row
dbCursor = dbConn.cursor()

def getModelTrainingInput():
    return

def getModelTrainingOutput():
    return

def getAnalysisTool():
    return

def testAnalyzer(tInput, tOutput, analyzer):
    return

def getPredictiveInput():
    return

def analyzeCurrentRestarauntModels(predictionInput, analyzer):
    return

def outputSchedule(inspectionSchedule):
    return

def main():
    # get the necessary components to build and use an analysis tool
    tInput = getModelTrainingInput()
    tOutput = getModelTrainingOutput()
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


    dbConn.close()

if __name__ == "__main__":
    main()
