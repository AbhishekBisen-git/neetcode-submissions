select distinct F.product_id , ifnull(B.new_price,10) as price
from products F left join 
(select A.product_id , A.new_price  from 
(select 
product_id,
row_number() over ( partition by product_id order by change_date desc ) as rnk,
new_price
from products
where change_date  <= '2019-08-16') A
WHERE A.rnk = 1) B
on F.product_id = B.product_id