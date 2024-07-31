# Write your MySQL query statement below
SELECT e1.employee_id
FROM Employees e1
LEFT JOIN Employees e2
ON e1.manager_id = e2.employee_id
WHERE e1.salary < 30000 and e2.employee_id is null and e1.manager_id is not null
ORDER BY e1.employee_id