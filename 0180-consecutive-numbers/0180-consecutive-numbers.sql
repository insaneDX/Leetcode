-- Write your PostgreSQL query statement below
select Distinct num as ConsecutiveNums
from (
    select num,
    LAG(num, 1) OVER (order by id) AS prev1, -- the number just before
    LAG(num, 2) OVER (order by id) AS prev2 -- the number 2 steps before
    from logs 
) t
where num = prev1
  and num = prev2;

-- | id | num | prev1 | prev2 |
-- | -- | --- | ----- | ----- |
-- | 1  | 1   | NULL  | NULL  |
-- | 2  | 1   | 1     | NULL  |
-- | 3  | 1   | 1     | 1     |
-- | 4  | 2   | 1     | 1     |

-- self join 3 times
-- select DISTINCT l1.num as ConsecutiveNums
-- FROM logs l1
-- JOIN Logs l2
--   On l1.id = l2.id - 1
-- Join Logs l3
--   On l2.id = l3.id - 1
-- where l1.num = l2.num
-- and l2.num = l3.num;
