# Write your MySQL query statement below

# movies with 1. odd number_id that is 2. not boring

SELECT *
FROM Cinema
WHERE id%2!=0 AND description!='boring'
ORDER BY rating DESC;