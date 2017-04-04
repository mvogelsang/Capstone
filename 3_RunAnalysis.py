import subprocess
import os
import sqlite3

# note, for convenience of writing many separate query functions
# the connection is defined globally
dbConn = sqlite3.connect("./LouData.db");
dbConn.row_factory = sqlite3.Row
dbCursor = dbConn.cursor()

# get violation totals for a year span returned in a list
# in the order [TOTAL VIOLATIONS, CRITICAL VIOLATIONS, NON-CRITICAL VIOLATIONS]
# and, of course total violations should equal critical + noncritical
# yearsback describes which year in the past you want results for.
# 1 would mean from today to 1 year ago, 2 would mean from the end
# one year ago to the end of two years ago (again, from today)
# so yearsback should never be less than one.
def getViolationTotals(business_id, yearsBack):
    queryArgs = (str(business_id), '"now", "-' + str(yearsBack) + ' years"')
    for r in dbCursor.execute("""select count(*)
                        from Health_Inspections_out as I, InspectionViolations_out as V
                        where I.establishment_id = ?
                            and I.inspection_id = V.inspection_id
                            and I.inspection_date > date(?)""", queryArgs):


def main():
    getViolationTotals( 33530, 10)
    getViolationTotals( 33768, 10)
    getViolationTotals( 0, 10)




if __name__ == "__main__":
    main()
