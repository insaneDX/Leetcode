-- Write your PostgreSQL query statement below

-- count ratings per user
(
    select u.name AS results
    FROM MovieRating mr
    JOIN Users u
        on mr.user_id = u.user_id
    GROUP BY u.name
    ORDER BY COUNT(*) DESC, u.name ASC
    LIMIT 1
)
UNION ALL
(
    SELECT m.title AS results
    FROM MovieRating mr
    JOIN Movies m
        ON mr.movie_id = m.movie_id
    where mr.created_at >= '2020-02-01'
        and mr.created_at < '2020-03-01'
    GROUP BY m.title
    ORDER BY AVG(mr.rating) DESC, m.title ASC
    LIMIT 1
);

-- USING RANK

-- FOR USER
-- SELECT name
-- FROM (
--     SELECT u.name,
--            RANK() OVER (ORDER BY COUNT(*) DESC, u.name ASC) AS rnk
--     FROM MovieRating mr
--     JOIN Users u
--       ON mr.user_id = u.user_id
--     GROUP BY u.name
-- ) t
-- WHERE rnk = 1;

--FOR MOVIE
-- SELECT title
-- FROM (
--     SELECT m.title,
--            RANK() OVER (ORDER BY AVG(mr.rating) DESC, m.title ASC) AS rnk
--     FROM MovieRating mr
--     JOIN Movies m
--       ON mr.movie_id = m.movie_id
--     WHERE mr.created_at >= '2020-02-01'
--       AND mr.created_at < '2020-03-01'
--     GROUP BY m.title
-- ) t
-- WHERE rnk = 1;