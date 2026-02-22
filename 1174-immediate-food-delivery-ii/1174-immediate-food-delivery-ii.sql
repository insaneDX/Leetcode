-- Write your PostgreSQL query statement below

SELECT 
    round(
        100.0 * sum(
            case
                when d.order_date = d.customer_pref_delivery_date THEN 1 ELSE 0 
            END
        ) / COUNT(*),
        2
    ) AS immediate_percentage
FROM Delivery d
-- get the min order_date per customer
JOIN (
    select customer_id, min(order_date) as first_order
    from Delivery
    Group by customer_id
    ) f
ON d.customer_id = f.customer_id
AND d.order_date = f.first_order;



-- window function
-- SELECT ROUND(
--         100.0 * SUM(
--             CASE 
--                 WHEN order_date = customer_pref_delivery_date THEN 1 
--                 ELSE 0 
--             END
--         ) / COUNT(*),
--         2
-- ) AS immediate_percentage
-- FROM (
--     SELECT *,
--            ROW_NUMBER() OVER (
--                PARTITION BY customer_id 
--                ORDER BY order_date
--            ) AS rn
--     FROM Delivery
-- ) t
-- WHERE rn = 1;