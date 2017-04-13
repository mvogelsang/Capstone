import sqlite3
import json
import sqlQueries

# JSON EXAMPLE ----------
# {
#     "Establishments": [{
#         "Establishment_Id": 3789327,
#         "Establishment_Name": "Example1",
#         "Establishment_Rank": 1
#     }, {
#         "Establishment_Id": 2124332,
#         "Establishment_Name": "Example2",
#         "Establishment_Rank": 2
#     }, {
#         "Establishment_Id": 49837587983,
#         "Establishment_Name": "SomethingElse",
#         "Establishment_Rank": 3
#     }]
# }
# --------------------------

# note, for convenience of writing many separate query functions
# the connection is defined globally
dbConn = sqlite3.connect("./LouData.db", detect_types=sqlite3.PARSE_DECLTYPES);
dbConn.row_factory = sqlite3.Row
dbCursor = dbConn.cursor()
dbCursor.executescript(sqlQueries.E_speedConfigure_0)

query = """
SELECT EstablishmentID as Establishment_Id,
PremiseName as Establishment_Name, 0 as Establishment_Rank from Establishments
limit 150
"""
dbCursor.execute(query)
res = dbCursor.fetchall()
arr = []
i = 1
for r in res:
    temp = {}
    temp['Establishment_Id'] = r[0]
    temp['Establishment_Name'] = r[1]
    temp['Establishment_Rank'] = i
    i += 1
    arr.append(temp)

final = {}
final['Establishments'] = arr
print json.dumps(final, indent=2)
dbCursor.close()
