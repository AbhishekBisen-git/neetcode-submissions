select distinct   c.employee_id  from 
employees a,
employees b,
employees c 
 where  
 a.manager_id = 1 and 
 c.employee_id !=1 and
 a.employee_id = b.manager_id and
 b.employee_id = c.manager_id  
