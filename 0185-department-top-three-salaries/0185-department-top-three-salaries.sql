-- Write your PostgreSQL query statement below
-- top 3 distinct salary ranks per department.
-- Ranking inside each department -> PARTITION BY departmentId

select d.name as Department, r.name as Employee, r.salary as Salary from 
(select *,
    dense_rank() over (partition by departmentid order by salary desc) as rnk
from Employee
) r
Join Department d
on d.id = r.DepartmentId
where r.rnk <= 3;