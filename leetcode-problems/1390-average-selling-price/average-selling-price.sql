# Write your MySQL query statement below
SELECT p.product_id, IF(u.product_id is not null, ROUND(SUM(p.price*u.units)/sum(u.units),2), 0) AS average_price
FROM Prices p 
LEFT JOIN UnitsSold u 
ON p.product_id = u.product_id 
WHERE u.purchase_date between p.start_date and p.end_date or u.product_id is null
GROUP BY p.product_id 