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

def main():
    # get analyzer and scaler
    with open("./pickles/analyzer.pickle", "rb") as input_file:
        analyzer = pickle.load(input_file)

    with open("./pickles/scaler.pickle", "rb") as input_file:
        scaler = pickle.load(input_file)

    daysaverage = []
    for month in range(2, 5):
        dbCursor.execute(sqlQueries.G_monthOfModels_2.format(farBound=(month+1), closeBound=(month)))
        data = dbCursor.fetchall()
        ldata = []
        actualOrder = []
        optimalOrder = []
        predictedOrder = []

        for item in data:
            lItem = list(item)
            ldata.append(lItem)
            actualOrder.append(lItem[0])


        del data

        orderGenerator = []
        for n in ldata:
            logit = numpy.array([n[1:7]])
            logit = scaler.transform(logit)
            pred = numpy.mean(analyzer.predict(logit))
            orderGenerator.append([n[0], pred, n[-1]])

        # begin building list of date differentials
        dayDiffs = []

        # put list of inspections in optimalOrder
        orderGenerator.sort(None, lambda x: x[2], False)
        for item in orderGenerator:
            optimalOrder.append(item[0])
        i = 0
        for inspection in actualOrder:
            dayDiffItem = []
            dayDiffItem.append(inspection)
            dayDiffItem.append(i)
            i = i + 1
            index = optimalOrder.index(inspection)
            dayDiffItem.append(index)
            score = orderGenerator[index][-1]
            if(score < 85):
                dayDiffItem.append(True)
            else:
                dayDiffItem.append(False)

            dayDiffs.append(dayDiffItem)


        # put list of inspections in predicted order
        orderGenerator.sort(None, lambda x: x[1], False)
        for item in orderGenerator:
            predictedOrder.append(item[0])
        i=0
        while i < len(dayDiffs):
            inspId = dayDiffs[i][0]
            dayDiffs[i].append(predictedOrder.index(inspId))
            i = i + 1

        # each daydiff now should have (inspection_id, actualOrderPlacement, optimalOrderPlacement, bool didFail, predictedOrderPlacement)
        # now let's get stats on the failed inspections
        failsPredictDiff = []
        for diffItem in dayDiffs:
            if(diffItem[3]):
                failsPredictDiff.append(diffItem[-1]-diffItem[1])
        print len(failsPredictDiff)
        print 'Average slots moved by failures: ' + str(numpy.mean(failsPredictDiff))
        print 'stddev slots moved by failures: ' + str(numpy.std(failsPredictDiff))
        print 'inspections this month: ' + str(len(predictedOrder))
        inspectionsperday = len(predictedOrder)/30
        dayssooner =float(numpy.mean(failsPredictDiff))/float(inspectionsperday)
        print 'average days sooner estimate: ' + str(dayssooner)
        print '\n'
        daysaverage.append(dayssooner)

    print 'average days sooner for test: ' + str(numpy.mean(daysaverage))




    dbConn.commit()
    dbConn.close()

if __name__ == "__main__":
    main()

# pickle_file will be closed at this point, preventing your from accessing it any further
