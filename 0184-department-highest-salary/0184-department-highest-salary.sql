-- Write your PostgreSQL query statement below
with ranked AS(
    select 
        name, 
        salary, 
        departmentId,
        DENSE_RANK() over (
            PARTITION BY departmentId
            ORDER BY salary DESC
        ) as rnk
    FROM Employee
)

select
    d.name as Department,
    r.name as employee,
    r.salary as salary

from ranked r
Join Department d
    ON r.departmentId = d.id
WHERE r.rnk = 1

