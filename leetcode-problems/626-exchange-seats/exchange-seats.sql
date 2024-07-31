# Write your MySQL query statement below
SELECT  
    CASE
        WHEN id%2=0 THEN id-1
        WHEN id = (SELECT MAX(id) FROM Seat) and id%2!=0  THEN id
        WHEN id%2!=0 THEN id+1
    END as id, 
    student
FROM Seat
ORDER BY ID;
