-- Write your PostgreSQL query statement below
SELECT c.name as Customers 
FROM Customers c
left Join Orders o
on c.id = o.customerId
where o.customerId IS NULL;

-- SELECT name AS Customers
-- FROM Customers c
-- WHERE NOT EXISTS (
--     SELECT 1
--     FROM Orders o
--     WHERE o.customerId = c.id
-- );