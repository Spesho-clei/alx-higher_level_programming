-- Use INNER JOIN
-- Execute: cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
SELECT cities.id, cities.name, states.name AS state_name
FROM cities, states
WHERE cities.state_id = states.id
ORDER BY cities.id ASC;
