select Department , Employee , Salary from 
(select

b.name as Department,
a.name as Employee,
a.salary as Salary ,
dense_rank() over (partition by b.name order by salary desc) as rnk 

from employee a left join department b
on
a.departmentId = b.id
)abc
where abc.rnk = 1
