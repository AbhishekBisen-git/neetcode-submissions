with cte as(

    select 
    driver_id,
    avg(distance_km/fuel_consumed) as klm,
    case when month(trip_date)<=6 then 1 else 2 end as quarter
    from trips
    group by quarter, driver_id

)

select
a.driver_id ,c.driver_name   , round(a.klm ,2)       as first_half_avg   ,
round(b.klm,2) as second_half_avg   , round(b.klm-a.klm,2) as efficiency_improvement 
 from 
cte a left  join cte b 
on a.quarter+1 = b.quarter and a.driver_id = b.driver_id
left join drivers c
on a.driver_id = c.driver_id
 where a.klm <b.klm 
 order by round(b.klm-a.klm,2) desc , 
 c.driver_name asc