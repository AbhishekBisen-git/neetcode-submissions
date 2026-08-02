 select 
 A.product_id,
 A.year as first_year,
 A.quantity as quantity , 
 A.price as price
 from sales A 
  join ( select product_id , min(year) as year from sales group by product_id) B on A.product_id = B.product_id and A.year = B.year




-- SELECT s.product_id,
--        s.year AS first_year,
--        s.quantity,
--        s.price
-- FROM Sales s
-- JOIN (
--     SELECT product_id, MIN(year) AS first_year
--     FROM Sales
--     GROUP BY product_id
-- ) t
-- ON s.product_id = t.product_id 
-- AND s.year = t.first_year;