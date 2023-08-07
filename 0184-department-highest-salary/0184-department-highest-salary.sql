# Write your MySQL query statement below


select
    d.name as Department, e.name as Employee, s.sal as Salary
from
    Employee e,
    (select departmentId, max(salary) as sal from Employee group by departmentId) s,
    Department d
where 
    e.salary = s.sal and
    e.departmentId = s.departmentId and
    d.id = s.departmentId
    
    