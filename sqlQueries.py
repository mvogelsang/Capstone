# all queries should end in '_#' where '#' is arguments they take in total
# this number should be inclusive of the amount needed by nested queries
# query arguments should be globally consistent (an argument name should be used in the same manner everywhere)
# if you are unsure what you are doing, make argument names globally unique

# this is a meta constant relevant to the sql table structure
# it should contain the table name, the row key,
# and the relevant view name for each table
# should have the form '(table, view, key)'
tableInfo = [ ('Establishments','V_relevantEstablishments_0', 'EstablishmentID'), ('Violations','V_relevantViolations_0','ODATAID'), ('Inspections','V_relevantInspections_0','inspection_id'), ('Addresses','V_relevantAddresses_0','FID'), ('ThreeOneOne','V_relevantThreeOneOne_0','service_request_id'), ('Crime','V_relevantCrime_0','INCIDENT_NUMBER') ]

# ----------------------------------  VIEWS  -----------------------------------
# these are subqueries that are meant to be used in other queries
# as such, they all use 'SELECT * FROM...', for compatibility
# as a principle, all non-view queries should specify columns to be selected
# and all view queries should select all columns.
# only non-view queries should be used in 'execute' statements
# they should all start with 'V_' in their name
# and their content should be surrounded in parentheses to facilitate usage

V_relevantEstablishments_0 = """
SELECT * FROM Establishments
WHERE EstablishmentID is not null and RCodeDesc is not null
and latitude != 0 and longitude != 0
and RCodeDesc LIKE '%FOOD SERVICE%'
and EstType LIKE 'FOOD SERVICE' and PremiseName not null
and PremiseStreet != 'MOBILE FOOD UNIT'
"""

V_relevantViolations_0 = """
SELECT * from Violations
WHERE inspection_id is not null and weight is not null
and critical_yn is not null
"""

V_relevantInspections_0 = """
SELECT * from Inspections
WHERE inspection_id is not null and establishment_id is not null
and inspection_date is not null and type is not null and score is not null and type !='FOLLOWUP'
"""

V_relevantAddresses_0 = """
SELECT * from Addresses
WHERE HOUSENO is not null and strname is not null and ZIPCODE is not null and x is not null and y is not null
"""

# this one should probably be investigated more
# it is cursory at best, it halfway should mimic
# the kind of 311 complaints that chicago keeps track of
V_relevantThreeOneOne_0 = """
SELECT * from ThreeOneOne
WHERE longitude is not null and latitude is not null and description is not null and requested_datetime is not null and service_name is not null
and ( description like '%GARBAGE%' or description like '%TRASH%' or description like '%JUNK%' or description like '%CART%' or description like '%RATS%' or description like '%FOOD%')
"""

# this one should also be evaluated more as well
V_relevantCrime_0 = """
SELECT * from Crime
WHERE INCIDENT_NUMBER is not null and DATE_OCCURED is not null and BLOCK_ADDRESS is not null and ZIP_CODE is not null
"""

# ---------------------------------  GETTERS  ----------------------------------
# these are non-view queries that only read data from the DB and have no
# permanent effect on it. They should start with 'G_'.

# ---------------------------------  EFFECTS  ----------------------------------
# these queries have effects on the db. they should start with 'E_'

# used for renaming the tables to something more sensible
E_tableRename_2 = "ALTER TABLE {current_name} RENAME TO {target_name}"

# used for cleaning out table rows that do not fit into our 'relevant' views
E_removeIrrelevant_3 = "DELETE from {table_name} where {table_name}.{key_name} not in (SELECT temp.{key_name} from ({view_query}) as temp)"


def main():
    for k,v in globals().iteritems():
        print k
        print v
        print '\n'

if __name__ == "__main__":
    main()
