import subprocess
import os

def loadData(csvfile):
    subprocess.call(["csvsql", "--db", "sqlite:///./LouData.db", "--insert", "--snifflimit", "1000", csvfile])


def main():
    datafiles = ["./clean_data/Establishments_out.csv","./clean_data/InspectionViolations_out.csv","./clean_data/Businesses_out.csv","./clean_data/Health_Inspections_out.csv","./clean_data/Address_Points_out.csv", "./clean_data/Citizen311data_7yrs_out.csv"]
    for df in datafiles:
        print "loading - " + df
        loadData(df)

if __name__ == "__main__":
    main()
