select A.firstName , A.lastName , B.city, B.state 
from
Person A left join address B on A.personId = B.personId