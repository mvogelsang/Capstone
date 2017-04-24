import subprocess
import os
import sqlite3
import datetime
import sqlQueries
import sklearn
from sklearn import preprocessing, metrics, model_selection, linear_model, svm
import pyglmnet
import numpy
import math
import pickle
from functools import partial

def getAggregatePrediction(arrGenerators, scalarGenerators, inputDataPoint):
    allPredictions = []
    for arrGen in arrGenerators:
        allPredictions.append(numpy.mean(arrGen.predict(inputDataPoint)))
    for scaleGen in scalarGenerators:
        allPredictions.append(scaleGen.predict(inputDataPoint))

    return numpy.mean(allPredictions)

# get analyzers and scaler
with open("./pickles/scaler.pickle", "rb") as input_file:
    scaler = pickle.load(input_file)
with open("./pickles/glmnet.pickle", "rb") as input_file:
    glmnet = pickle.load(input_file)
with open("./pickles/ardRegressor.pickle", "rb") as input_file:
    ardRegressor = pickle.load(input_file)
with open("./pickles/svrRegressor.pickle", "rb") as input_file:
    svrRegressor = pickle.load(input_file)

getPrediction = partial(getAggregatePrediction, [glmnet], [ardRegressor, svrRegressor])
