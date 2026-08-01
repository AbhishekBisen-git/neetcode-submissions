select A.Department , A.Employee , A.Salary
from
(select 

department.name as Department,
employee.name as Employee,
employee.salary as Salary,
dense_rank() over (partition by department.name order by employee.salary desc) as 'r'


from employee
inner join department on 
employee.departmentId = department.id
) A
where A.r=1