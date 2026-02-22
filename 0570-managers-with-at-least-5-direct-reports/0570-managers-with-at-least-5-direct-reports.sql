-- Write your PostgreSQL query statement below
select e.name 
from Employee e
-- count employees per manager
Join
(
    select managerId
    FROM Employee
    GROUP BY managerId
    HAVING Count(*) >= 5
) m 
on e.id = m.managerId;