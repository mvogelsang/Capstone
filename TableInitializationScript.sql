--this file is mostly for reference

PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE "Establishments" (
	"EstablishmentID" DECIMAL,
	"RCodeDesc" VARCHAR,
	"EstType" VARCHAR,
	"PremiseName" VARCHAR,
	opening_date TIMESTAMP,
	latitude DECIMAL,
	longitude DECIMAL
);
CREATE TABLE "Violations" (
	"ODATAID" DECIMAL,
	inspection_id DECIMAL,
	weight DECIMAL,
	critical_yn BOOLEAN,
	CHECK (critical_yn IN (0, 1))
);
CREATE TABLE "Inspections" (
	inspection_id DECIMAL,
	establishment_id DECIMAL,
	inspection_date TIMESTAMP,
	type VARCHAR,
	score DECIMAL
);
CREATE TABLE "Addresses" (
	"FID" DECIMAL,
	"HOUSENO" DECIMAL,
	"DIR" VARCHAR,
	"STRNAME" VARCHAR,
	"TYPE" VARCHAR,
	"ZIPCODE" DECIMAL,
	"X" DECIMAL,
	"Y" DECIMAL
);
CREATE TABLE "ThreeOneOne" (
	service_request_id DECIMAL,
	description VARCHAR,
	service_name VARCHAR,
	longitude DECIMAL,
	latitude DECIMAL,
	requested_datetime TIMESTAMP
);
CREATE TABLE "Crime" (
	"INCIDENT_NUMBER" VARCHAR,
	"DATE_OCCURED" TIMESTAMP,
	"BLOCK_ADDRESS" VARCHAR,
	"CITY" VARCHAR,
	"ZIP_CODE" VARCHAR
);

COMMIT;
