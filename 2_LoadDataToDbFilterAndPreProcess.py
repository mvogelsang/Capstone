import subprocess
import os
import sqlite3
import datetime

def dbConnect():
    dbConn = sqlite3.connect("./LouData.db", detect_types=sqlite3.PARSE_DECLTYPES);
    dbConn.row_factory = sqlite3.Row
    return dbConn

def loadData(csvfile):
    subprocess.call(["csvsql", "--db", "sqlite:///./LouData.db", "--insert", "--snifflimit", "1000", csvfile])

def main():
    datafiles = ["./clean_data/Establishments_out.csv","./clean_data/InspectionViolations_out.csv","./clean_data/Health_Inspections_out.csv","./clean_data/Address_Points_out.csv", "./clean_data/Citizen311data_7yrs_out.csv", "./clean_data/Crime_out.csv"]
    for df in datafiles:
        print "loading - " + df
        loadData(df)

    print 'data loaded, beginning preprocessing'
    # cleanAddressPoints()
    # clean311()
    # cleanCrime()
    # cleanEstablishments()
    # cleanInspections()
    # cleanViolations()
    renameTables()

if __name__ == "__main__":
    main()
