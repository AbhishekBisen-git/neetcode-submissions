SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT
        id,
        num,
        LAG(num, 1) OVER (ORDER BY id) AS previous_num,
        LAG(num, 2) OVER (ORDER BY id) AS two_rows_before
    FROM Logs
) t
WHERE num = previous_num
  AND num = two_rows_before;