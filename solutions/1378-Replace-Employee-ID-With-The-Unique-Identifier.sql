# Write your MySQL query statement below
select unique_id, name
from EmployeeUNI u right outer join Employees e
on u.id = e.id;
