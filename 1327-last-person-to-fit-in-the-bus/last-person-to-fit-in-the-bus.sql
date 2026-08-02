select person_name from 
(
select 
sum(weight) over ( order by turn ) as 'weight1',
person_name ,
weight 

from queue
order by turn
) ABC
where ABC.weight1<=1000
order by ABC.weight1 desc
limit 1