import subprocess
import os
import sqlite3
import datetime

# note, for convenience of writing many separate query functions
# the connection is defined globally
dbConn = sqlite3.connect("./LouData.db", detect_types=sqlite3.PARSE_DECLTYPES);
dbConn.row_factory = sqlite3.Row
dbCursor = dbConn.cursor()

# get violation totals for a year span returned in a list
# in the order [TOTAL VIOLATIONS, CRITICAL VIOLATIONS, NON-CRITICAL VIOLATIONS]
# and, of course total violations should equal critical + noncritical
# yearsback describes which year in the past you want results for.
# 1 would mean from today to 1 year ago, 2 would mean from the end
# one year ago to the end of two years ago (again, from today)
# so yearsback should never be less than one.
# also we aren't be ridiculously accurate about leapdays, but that
# would be far more trouble than it's worth
def getViolationTotals(business_id, yearsBack):
    daysBack = int(365.25*yearsBack)
    now = datetime.date.today()
    timeBegin = now - datetime.timedelta(days=daysBack)
    timeEnd = now - datetime.timedelta(days=(daysBack-365))
    queryArgs = (str(business_id), timeBegin, timeEnd)
    dbCursor.execute("""select count(*)
                        from Health_Inspections_out as I, InspectionViolations_out as V
                        where I.establishment_id = ?
                            and I.inspection_id = V.inspection_id
                            and I.inspection_date > ?
                            and I.inspection_date < ?
                            and V.critical_yn is not null
                            and I.score is not null;""", queryArgs)
    # print dbCursor.fetchall()


def main():
    getViolationTotals( 33530, 1)
    getViolationTotals( 33768, 1)
    getViolationTotals( 0, 1)
    y = '%' + 'W' + '%'
    dbCursor.execute("select (dir|| ' ' || strname) as hm from address_points_out where dir is not null and hm like(?)", (y,))
    x = dbCursor.fetchall()
    for i in x:
        print i




if __name__ == "__main__":
    main()
