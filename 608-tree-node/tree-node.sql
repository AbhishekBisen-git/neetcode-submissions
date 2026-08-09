select  

id , 
case
when  p_id is null then 'Root' 
when id not in ( select distinct p_id from tree) then 'Leaf' 
when id in ( select distinct p_id from tree) then 'Inner' 
else 'Leaf'

end as type



from
tree