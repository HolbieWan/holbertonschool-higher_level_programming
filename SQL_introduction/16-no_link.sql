-- Commands to list all records from the table second_table except rows without a name value
SELECT score, name FROM second_table WHERE name IS NOT NULL
ORDER BY score DESC;
