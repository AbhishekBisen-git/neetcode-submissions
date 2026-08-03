select department as Department , name as Employee , salary as Salary from (
select b.name as department , a.name , a.salary 
, dense_rank() over (partition by b.name order by a.salary desc) as 'r'
from employee a left join department b on
a.departmentId = b.id) 
abc where r<=3
 
