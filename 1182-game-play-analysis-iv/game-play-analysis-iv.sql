select 
round(count(distinct a.player_id)/(select count(distinct player_id) from activity),2) as fraction
from activity a join activity b 
on a.event_date = date_add(b.event_date,interval -1 day)
and a.player_id = b.player_id
and a.event_date = (
    SELECT MIN(event_date)
    FROM Activity
    WHERE player_id = a.player_id
)