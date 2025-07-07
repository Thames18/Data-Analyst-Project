-- SQLite query example
-- To run: sqlite3 customers.db < query.sql

SELECT country, COUNT(*) AS num_customers, AVG(age) AS avg_age
FROM customers
GROUP BY country
ORDER BY num_customers DESC;
