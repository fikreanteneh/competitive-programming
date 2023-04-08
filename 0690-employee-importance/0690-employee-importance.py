"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employe = None
        self.importance = 0
        mapEmp = {}
        for employee in employees:
            mapEmp[employee.id] = employee
            if employee.id == id:
                employe = employee
        
        def solution(employee):
            self.importance += employee.importance
            for i in employee.subordinates:
                solution(mapEmp[i])
        
        
        solution(employe)
        return self.importance