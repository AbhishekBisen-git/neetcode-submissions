select distinct b.product_id from
(select * ,
case when a.cnt>=3 and
lead(a.cnt,1) over (partition by a.product_id order by a.yyr desc) >=3 and
lead(a.yyr,1) over (partition by a.product_id order by a.yyr desc) = a.yyr-1
then a.product_id else NULL end as jkl
from
(select 
product_id , 
year(purchase_date) as yyr, 
count(*) as cnt
from 
orders
group by product_id , year(purchase_date)) A)b
where 
b.jkl is not null   
