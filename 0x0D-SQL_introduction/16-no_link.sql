-- List all records of table second_table
USE hbtn_0c_0;

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
