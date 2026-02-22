CREATE OR REPLACE FUNCTION NthHighestSalary(N INT) RETURNS TABLE (Salary INT) AS $$
BEGIN
 -- edge case where argument was passed as -1
    IF N <= 0 THEN
            RETURN QUERY SELECT NULL::INT;
            RETURN;
    END IF;

  RETURN QUERY(
    
    SELECT distinct e.Salary
    from employee e
    ORDER BY e.Salary Desc
    Limit 1 OFFSET N-1
      
  );
END;
$$ LANGUAGE plpgsql;


-- SELECT salary
--         FROM (
--             SELECT salary,
--                    DENSE_RANK() OVER (ORDER BY salary DESC) AS rnk
--             FROM Employee
--         ) t
--         WHERE rnk = N
--         LIMIT 1
--     );