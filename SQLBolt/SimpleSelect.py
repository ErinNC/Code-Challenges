# Review 1


# List all the Canadian cities and their populations
SELECT city, population
FROM north_american_cities
WHERE country LIKE 'Canada';

# Order all the cities in the United States by their latitude from north to south
SELECT city, latitude
FROM north_american_cities
WHERE country LIKE 'United States'
ORDER BY latitude DESC;

# List all the cities west of Chicago, ordered from west to east
SELECT city, longitude 
FROM north_american_cities
WHERE longitude < -87.629798
ORDER BY longitude ASC;

# List the two largest cities in Mexico (by population)
SELECT *
FROM north_american_cities
WHERE country LIKE 'Mexico'
ORDER BY population DESC
LIMIT 2;

# List the third and fourth largest cities (by population) in the United States and their population
SELECT city, population 
FROM north_american_cities
WHERE country LIKE 'United States'
ORDER BY population DESC
LIMIT 2 OFFSET 2;
