import subprocess
import os
import sqlite3
import datetime
import sqlQueries

# note, for convenience of writing many separate query functions
# the connection is defined globally
dbConn = sqlite3.connect("./LouData.db", detect_types=sqlite3.PARSE_DECLTYPES);
dbConn.row_factory = sqlite3.Row
dbCursor = dbConn.cursor()
dbCursor.executescript(sqlQueries.E_speedConfigure_0)

def main():
    # create the model table (delete if it already exists and restart)
    print 'creating model table...'
    dbCursor.executescript(sqlQueries.E_createModelTable_0)
    print'...'
    dbConn.commit()

    # put basic information into the model table
    print 'filling in basic model information...'
    dbCursor.execute(sqlQueries.E_startModelInfo_0)
    print'...'
    dbConn.commit()

    # fill in average information to model
    print 'getting averages...'
    dbCursor.execute(sqlQueries.E_fillInModelAverages_0)
    print'...'
    dbConn.commit()

    # fill in recent information to model
    print 'getting recent information...'
    dbCursor.execute(sqlQueries.E_fillInModelRecentValues_0)
    print'...'
    dbConn.commit()


    # fill in the (potentially useful) model powerscore statistics
    print 'filling in power scores...'
    dbCursor.execute(sqlQueries.E_calculatePowerScores_0)
    print'...'
    dbConn.commit()

    # end of run
    print "finishing"
    dbConn.commit()
    dbConn.close()


if __name__ == "__main__":
    main()
