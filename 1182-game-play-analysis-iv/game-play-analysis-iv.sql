select round(sum(abc.fraction)/(select count(distinct player_id) from Activity),2) as fraction from
(select  

case when datediff (lag(event_date,1) over (partition by player_id order by event_date asc),event_date) = -1  and row_number() over (partition by player_id order by event_date asc) = 2 then 1 else 0 end  as fraction
from Activity
) abc

