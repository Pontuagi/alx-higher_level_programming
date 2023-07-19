-- Compute score avarage of all records in second_table
USE %S;
SELECT AVG(score) AS average
FROM second_table;
