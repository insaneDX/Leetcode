-- Write your PostgreSQL query statement below

Select 
    ROUND(
        COUNT(DISTINCT a.player_id)::decimal / (select count(Distinct player_id) from Activity), 2
    ) as fraction
from Activity a
join
--find first login per player
(
    select player_id, min(event_date) as first_login
    from Activity
    Group by player_id
) f
ON a.player_id = f.player_id
AND a.event_date = f.first_login + INTERVAL '1 day';

-- why DISTINCT
-- Because a player might log in multiple times on that next day. We count player only once.
