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

def loadData(csvfile):
    subprocess.call(["csvsql", "--db", "sqlite:///./LouData.db", "--insert", "--snifflimit", "1000", csvfile])

def renameTables(renameArr):
    for tup in renameArr:
        dbCursor.execute(sqlQueries.E_tableRename_2
                            .format(current_name=tup[0], target_name=tup[1])
                        )
def removeIrrelevant(tableInformation):
    for table in tableInformation:
        dbCursor.execute(sqlQueries.E_removeIrrelevant_3
                            .format(table_name=table[0], key_name=table[2], view_query=getattr(sqlQueries, table[1]))
        )

def main():
    # load the csv's to the database
    datafiles = ["./clean_data/Establishments_out.csv","./clean_data/InspectionViolations_out.csv","./clean_data/Health_Inspections_out.csv","./clean_data/Address_Points_out.csv", "./clean_data/Citizen311data_7yrs_out.csv", "./clean_data/Crime_out.csv"]
    for df in datafiles:
        print "loading - " + df
        loadData(df)

    # give tables more usable names for queries
    print 'data loaded, beginning preprocessing'
    renameTables([('Establishments_out', 'Establishments'), ('InspectionViolations_out', 'Violations'),('Health_Inspections_out', 'Inspections'),('Address_Points_out', 'Addresses'),('Citizen311data_7yrs_out', 'ThreeOneOne'),('Crime_out', 'Crime')])

    # remove irrelevant rows (as deemed by relevance in the sqlQueries file)
    removeIrrelevant(sqlQueries.tableInfo)

    # end of run
    print "finishing"
    dbConn.commit()
    dbConn.close()



if __name__ == "__main__":
    main()
