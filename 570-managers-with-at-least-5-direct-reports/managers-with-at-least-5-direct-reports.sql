select name from 
(select 
a.name ,  count(a.id) as cnt
from
employee a
inner join
employee b  on 
a.id = b.managerId
group by a.id) abc
where abc.cnt >=5