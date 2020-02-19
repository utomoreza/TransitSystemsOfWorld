createCities = "CREATE TABLE cities(
	id INTEGER PRIMARY KEY,
	name CHAR(50),
	coords VARCHAR(100),
	start_year INTEGER,
	url_name CHAR(50),
	country CHAR(50),
	country_state CHAR(50));"

copyCities = "COPY cities(id,
	name,
	coords,
	start_year,
	url_name,
	country,
	country_state) 
FROM '/home/utomoreza/Projects/TransitSystemsOfWorld_Python/datasets/cities.csv' 
DELIMITER ',' CSV HEADER;"


createLines = "CREATE TABLE lines(
	);"