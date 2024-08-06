# Write your MySQL query statement below
SELECT p.project_id, ROUND(AVG(e.experience_years),2) average_years
FROM project p
LEFT JOIN Employee e
ON e.employee_id = p.employee_id
GROUP BY project_id;