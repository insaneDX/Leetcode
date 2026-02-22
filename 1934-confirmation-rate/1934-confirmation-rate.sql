-- Write your PostgreSQL query statement below
select
    s.user_id, 
    ROUND(
        COALESCE(
            COUNT (case when c.action = 'confirmed' then 1 end) :: decimal / NULLIF(COUNT(c.action), 0), 0
        ), 2
    ) as confirmation_rate -- Count Confirmed Attempts
    
FROM signups s -- Start with all users who signed up
LEFT JOIN Confirmations c
    ON s.user_id = c.user_id
GROUP BY s.user_id -- For each user, calculate their success rate
ORDER BY s.user_id;


-- Count Total Attempts
-- COUNT(c.action)
-- confirmed_count / total_count
-- If result is NULL → replace with 0.

-- NULLIF(COUNT(c.action), 0)
-- This means:

-- If total_count = 0 → return NULL instead of 0.

-- So division becomes:
-- something / NULL
-- Which results in NULL (safe).