-- lists all the rows of value name
SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;