# Write your MySQL query statement below
with summary as (
  SELECT departmentId , name , Salary ,
  DENSE_RANK() OVER (PARTITION BY departmentId ORDER BY Salary desc) as rnk
from Employee
)

SELECT d.name as Department, s.name as Employee, s.Salary   from summary s 
Join Department d
on d.id = s.departmentId
 where rnk <= 3