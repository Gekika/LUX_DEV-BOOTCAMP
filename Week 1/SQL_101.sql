-- An example of the select query where we will filter out names of 
-- employees whos age is above 30 ....from the Employees table
-- SELECT query for retreving

SELECT name, age
FROM employees
WHERE age > 30 

-- INSERT query to insert data
-- This help us add more data to the table
-- we have to be specific on how data is structured

INSERT INTO employees (name, age, department)
VALUES ('John Doe', 35, 'IT')



-- UPDATE query to modify data
-- This helps us update existing data in the table
-- we have to be specific on which row we want to update

UPDATE employees
SET age = 30
WHERE name = 'John Doe'

-- DELETE query to remove data
-- This helps us remove existing data from the table
DELETE FROM employees
WHERE age < 25

-- ALTER query to modify table structure
-- This helps us add or remove columns from the table
ALTER TABLE employees
ADD COLUMN email VARCHAR(255) NOT NULL


--Aggregation using COUNT function
SELECT department, COUNT(*)
FROM employees
GROUP BY department


