# Write your MySQL query statement below

# SELECT Name AS Employee
# FROM Employee
# WHERE salary > (
#     SELECT salary
#     FROM Employee AS Manager
#     WHERE Manager.Id = Employee.ManagerId
# );

SELECT e1.Name as Employee
FROM Employee as e1, Employee as e2
WHERE e1.ManagerId = e2.Id 
  AND e1.Salary > e2.Salary;

