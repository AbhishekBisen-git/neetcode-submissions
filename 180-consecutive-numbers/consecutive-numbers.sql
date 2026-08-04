select b.n3 as ConsecutiveNums  from
(select DISTINCT (case when a.num=a.n1 and a.n1=a.n2 then a.num else null end) as n3
from

(select num,
lead(num,1) over (order by id) as n1,
lead(num,2) over (order by id) as n2
from logs) a)b
WHERE b.n3 is not null