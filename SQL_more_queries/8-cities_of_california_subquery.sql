-- script that lists all the cities of California that can be found in the database hbtn_0d_usa.
SELECT cities.name from cities where state_id = (SELECT id from states where name = 'California')
ORDER BY cities.id ASC;
