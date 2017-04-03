-- THIS FILE IS SOLELY USED FOR REFERENCE
-- IT IS NOT DYNAMICALLY GENERATED OR USED ANYWHERE

CREATE TABLE Address_Points_out (
	"FID" DECIMAL NOT NULL,
	"HOUSENO" DECIMAL NOT NULL,
	"DIR" VARCHAR(1),
	"STRNAME" VARCHAR(20) NOT NULL,
	"ZIPCODE" DECIMAL NOT NULL,
	"X" DECIMAL NOT NULL,
	"Y" DECIMAL NOT NULL
);

CREATE TABLE Businesses_out (
	business_id DECIMAL NOT NULL,
	name VARCHAR(52) NOT NULL,
	latitude DECIMAL NOT NULL,
	longitude DECIMAL NOT NULL
);

CREATE TABLE Citizen311data_7yrs_out (
	service_request_id DECIMAL NOT NULL,
	description VARCHAR(72) NOT NULL,
	service_name VARCHAR(16) NOT NULL,
	longitude DECIMAL,
	latitude DECIMAL,
	requested_datetime TIMESTAMP
);

CREATE TABLE Establishments_out (
	"EstablishmentID" DECIMAL NOT NULL,
	"RCodeDesc" VARCHAR(40) NOT NULL,
	"EstType" VARCHAR(42) NOT NULL,
	"PremiseName" VARCHAR(50) NOT NULL,
	opening_date TIMESTAMP,
	latitude DECIMAL NOT NULL,
	longitude DECIMAL NOT NULL
);

CREATE TABLE Health_Inspections_out (
	inspection_id DECIMAL NOT NULL,
	establishment_id DECIMAL,
	score DECIMAL NOT NULL
);

CREATE TABLE InspectionViolations_out (
	"ODATAID" DECIMAL NOT NULL,
	inspection_id DECIMAL NOT NULL,
	weight DECIMAL NOT NULL,
	critical_yn BOOLEAN NOT NULL,
	CHECK (critical_yn IN (0, 1))
);
