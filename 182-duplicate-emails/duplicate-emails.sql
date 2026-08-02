select distinct A.email from 
(select email , count(*) as 'rn' from person
group by email
)A
where A.rn >1