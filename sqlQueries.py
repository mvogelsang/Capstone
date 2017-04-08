def clean311():
    print 'processing 311 data'
    conn = dbConnect()
    c = conn.cursor()

    # get rid of inappropriate blanks and nulled rows
    c.execute("delete from Citizen311data_7yrs_out where service_request_id is null or description is null or longitude is null or latitude is null or requested_datetime is null")
    c.execute("delete from Citizen311data_7yrs_out where service_request_id is '' or description is '' or longitude is '' or latitude is '' or requested_datetime is '' or longitude is 0 or latitude is 0")

    # get rid of complaints that are not pertinent (must be health/sanitation related)
    keywords = ['GARBAGE','TRASH','JUNK', 'CART', 'RATS', 'FOOD']
    for word in keywords:
        queryFill = '%'+word+'%'
        c.execute("delete from Citizen311data_7yrs_out where description not like(?) and service_name not like(?)", (queryFill, queryFill))

    # get rid of data older than ~10 yrs
    now = datetime.date.today()
    timeEdge = now - datetime.timedelta(days=10*365.25)
    c.execute("delete from Citizen311data_7yrs_out where requested_datetime < ?", (timeEdge,))

# all queries should end in '_#' where '#' is arguments they take in total
# this number should be inclusive of the amount needed by nested queries



# ----------------------------------  VIEWS  -----------------------------------
# these are subqueries that are meant to be used in other queries
# as such, they all use 'SELECT * FROM...', for compatibility
# as a principle, all non-view queries should specify columns to be selected
# and all view queries should select all columns.
# only non-view queries should be used in 'execute' statements
# they should all start with 'V_' in their name
# and their content should be surrounded in parentheses to facilitate usage

V_relevantRestaraunts_0 =




# ---------------------------------  GETTERS  ----------------------------------
# these are non-view queries that only read data from the DB and have no
# permanent effect on it. They should start with 'G_'.

# ---------------------------------  EFFECTS  ----------------------------------
# these queries have effects on the db. they should start with 'E_'
