# Write your MySQL query statement below

# movies with 1. odd number_id that is 2. not boring

SELECT *
FROM (SELECT * FROM Cinema WHERE id%2!=0) as d
WHERE d.description!='boring'
ORDER BY d.rating DESC;