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

def cleanAddressPoints():
    conn = dbConnect()


def clean311():
    print 'processing 311 data'
    conn = dbConnect()
    c = conn.cursor()

    # get rid of inappropriate blanks and nulled rows
    c.execute("delete from Citizen311data_7yrs_out where service_request_id is null or description is null or longitude is null or latitude is null or requested_datetime is null")
    c.execute("delete from Citizen311data_7yrs_out where service_request_id is '' or description is '' or longitude is '' or latitude is '' or requested_datetime is '' or longitude is 0 or latitude is 0")

    # get rid of complaints that are not pertinent (must be health/sanitation related)
    keywords = ['GARBAGE','TRASH','JUNK', 'DEAD', 'CART', 'RATS', 'FOOD']
    for word in keywords:
        queryFill = '%'+word+'%'
        c.execute("delete from Citizen311data_7yrs_out where description not like(?) and service_name not like(?)", (queryFill, queryFill))

    # get rid of data older than ~10 yrs
    now = datetime.date.today()
    timeEdge = now - datetime.timedelta(days=10*365.25)
    c.execute("delete from Citizen311data_7yrs_out where requested_datetime < ?", (timeEdge,))


# def cleanCrime():
#
#     INCIDENT_NUMBER
#     DATE_OCCURED
#     BLOCK_ADDRESS
#     CITY
#     ZIP_CODE
# def cleanEstablishments():
#
# def cleanInspections():
#
# def cleanViolations():


def main():
    datafiles = ["./clean_data/Establishments_out.csv","./clean_data/InspectionViolations_out.csv","./clean_data/Health_Inspections_out.csv","./clean_data/Address_Points_out.csv", "./clean_data/Citizen311data_7yrs_out.csv", "./clean_data/Crime_out.csv"]
    for df in datafiles:
        print "loading - " + df
        loadData(df)

    print 'data loaded, beginning preprocessing'
    cleanAddressPoints()
    clean311()
    cleanCrime()
    cleanEstablishments()
    cleanInspections()
    cleanViolations()

if __name__ == "__main__":
    main()
