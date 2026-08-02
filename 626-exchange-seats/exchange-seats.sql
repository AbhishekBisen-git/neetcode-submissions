select A.id , A.student from 
(select student , case 
when id = (select max(id) from seat) and id%2 = 1 then id
when id%2 = 1 
then id+1 
else id-1 end as 'id' from seat
) A
order by A.id asc