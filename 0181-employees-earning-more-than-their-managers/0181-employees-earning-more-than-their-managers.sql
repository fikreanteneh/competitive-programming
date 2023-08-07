# Write your MySQL query statement below

SELECT name AS Employee
FROM Employee
WHERE salary > (
    SELECT salary
    FROM Employee AS Manager
    WHERE Manager.Id = Employee.ManagerId
);