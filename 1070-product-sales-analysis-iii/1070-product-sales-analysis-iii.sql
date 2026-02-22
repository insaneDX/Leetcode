-- Write your PostgreSQL query statement below
select s.product_id,f.first_year, s.quantity, s.price  
from sales s
-- query to fetch the min year data
Join
(
    select product_id, min(year) as first_year 
    from sales
    group by product_id
) f
on s.product_id = f.product_id
and s.year = f.first_year