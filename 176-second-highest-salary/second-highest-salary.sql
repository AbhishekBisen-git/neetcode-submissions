select (
select

distinct salary as SecondHighestSalary 
from

(select 
salary , 
dense_rank() over (order by salary desc) as rnk 

from employee) abc
where abc.rnk = 2)
AS SecondHighestSalary;
