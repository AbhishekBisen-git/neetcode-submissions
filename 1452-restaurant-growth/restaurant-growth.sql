-- SELECT visited_on, amount, average_amount 
-- FROM (
-- SELECT DISTINCT visited_on, SUM(amount) OVER
--  (ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW) AS amount,
--   ROUND(SUM(amount) OVER (ORDER BY visited_on RANGE BETWEEN INTERVAL 6 DAY PRECEDING AND CURRENT ROW)/7,2)
--    AS average_amount
-- FROM Customer) as whole_totals
-- WHERE DATEDIFF(visited_on, (SELECT MIN(visited_on) FROM Customer)) >= 6

select * from 
(
select 
visited_on,
sum(amount) over ( order by  visited_on range between interval 6 day preceding and current row) as 'amount',
round((sum(amount) over (order by visited_on range between interval 6 day preceding and current row))/7,2) as 'average_amount'
from customer ) ABC
where datediff(ABC.visited_on,(select min(visited_on) from customer))>=6
group by ABC.visited_on 