-- Write your PostgreSQL query statement below
select w1.id
from Weather w1
Join Weather w2
on w1.recorddate = w2.recorddate + INTERVAL '1 DAY'
Where w1.temperature > w2.temperature

-- today_date = yesterday_date + 1 day by using this self join is made

-- SELECT w1.id
-- FROM Weather w1
-- JOIN Weather w2
-- ON w1.recordDate = w2.recordDate + 1
-- WHERE w1.temperature > w2.temperature;