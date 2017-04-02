import subprocess
import os

def getColsAccumulateAndClean(filenames, columns, destination):
    # generate temp filenames, store them, and fill them
    tempnames = []
    for dfile in filenames:
        tempnames.append(dfile+".temp.csv")
        tempfile = open(dfile+".temp.csv", "w")
        command = ["csvcut", "-x", "-c"] + [",".join(columns)] + [dfile]
        print "cutting... " + " ".join(command)
        proc = subprocess.call(command, stdout=tempfile )
        tempfile.close()

    # now that columns are pulled, stack the separate files together
    print "stacking..."
    stackedfile = open(destination, "w")
    proc = subprocess.call(["csvstack"] + tempnames, stdout=stackedfile )
    stackedfile.close()

    # remove temporary files
    print "cleaning temporary files..."
    for dfile in tempnames:
        os.remove(dfile)

    # clean the output file
    print "cleaning data..."
    proc = subprocess.call(["csvclean", destination])

    # the REAL destination is really destination_out.csv (out is added by the cleaning process)
    # remove the old destination, and just keep the csvclean one
    os.remove(destination)

def main():
    # do initial preparation of the 311 data
    fileList311 = ["./raw_data/citizen311data_1.csv", "./raw_data/citizen311data_2.csv", "./raw_data/citizen311data_3.csv", "./raw_data/citizen311data_4.csv", "./raw_data/citizen311data_5.csv", "./raw_data/citizen311data_6.csv", "./raw_data/citizen311data_7.csv"]
    cols = ["service_request_id", "description", "service_name", "longitude", "latitude", "requested_datetime"]
    dest = "./clean_data/Citizen311data_7yrs.csv"
    getColsAccumulateAndClean(fileList311, cols, dest)

    # do initial prep of establishment table
    fileListHealthEst = ["./raw_data/Health_Establishments.csv"]
    cols = ["EstablishmentID", "RCodeDesc", "EstType", "PremiseName", "opening_date", "latitude", "longitude"]
    dest = "./clean_data/Establishments.csv"
    getColsAccumulateAndClean(fileListHealthEst, cols, dest)

    # do initial prep of the Inspections Violations table
    fileListHealthInspViolations = ["./raw_data/Health_InspViolations.csv"]
    cols = ["ODATAID","inspection_id","weight","critical_yn"]
    dest = "./clean_data/InspectionViolations.csv"
    getColsAccumulateAndClean(fileListHealthInspViolations, cols, dest)

if __name__ == "__main__":
    main()
