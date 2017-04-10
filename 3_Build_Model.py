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
    dbCursor.executescript(sqlQueries.E_createModelTable_0)

    # put basic information into the model table
    dbCursor.execute(sqlQueries.E_startModelInfo_0)

    # fill in average information to model
    dbCursor.execute(sqlQueries.E_fillInModelRecentValues_0)

    # fill in the (potentially useful) model powerscore statistics
    dbCursor.execute()

    # end of run
    print "finishing"
    dbConn.commit()
    dbConn.close()


if __name__ == "__main__":
    main()
