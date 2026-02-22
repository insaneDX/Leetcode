-- Write your PostgreSQL query statement below
-- second highest distinct salary and also works for to Find Nth highest salary
-- select (
--     select Distinct salary
--     From employee
--     order by Salary desc
--     LIMIT 1 OFFSET 1
-- )
-- as SecondHighestSalary

-- Working 
-- DISTINCT → remove duplicates
-- ORDER BY DESC → largest first
-- OFFSET 1 → skip highest
-- LIMIT 1 → take next

-- select max(salary) as SecondHighestSalary
-- FROM EMPLOYEE
-- Where Salary < (
--     select max(salary) from Employee
-- )

-- Third highest salary using max (Nested logic)
-- SELECT MAX(salary) AS ThirdHighestSalary
-- FROM Employee
-- WHERE salary < (
--     SELECT MAX(salary)
--     FROM Employee
--     WHERE salary < (
--         SELECT MAX(salary)
--         FROM Employee
--     )
-- );

select (
    select DISTINCT salary
    from (
        select salary, 
        dense_rank() over (order by salary DESC) as rnk 
        from Employee
    ) T
    where rnk = 2
) AS SecondHighestSalary;