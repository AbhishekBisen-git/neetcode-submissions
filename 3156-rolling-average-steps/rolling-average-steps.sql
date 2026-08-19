select 
 abc.user_id ,abc.steps_date , abc.rolling_average
 from

(select 
user_id , 
steps_date,
round(avg(steps_count) over ( partition by user_id order by steps_date asc rows between 2 preceding  and current row),2) as rolling_average ,
case when datediff(lag(steps_date,2) over (partition by user_id order by steps_date),steps_date )= -2 then 1 else 0 end as flg
from 
Steps
) abc
where abc.flg = 1