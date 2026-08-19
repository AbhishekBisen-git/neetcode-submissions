with cte1 as (
select 
product_id,
sum(spend) as spend,
year(transaction_date) as year 

from user_transactions
group by year(transaction_date) , product_id
order by year(transaction_date) asc
)

select 
year ,
product_id ,
spend as curr_year_spend,
lag(spend,1) over (partition by product_id order by year  asc ) as prev_year_spend,
round((((spend-(lag(spend,1) over (partition by product_id order by year  asc )))/(lag(spend,1) over (partition by product_id order by year  asc )))*100),2) as yoy_rate 
   
from 
cte1 