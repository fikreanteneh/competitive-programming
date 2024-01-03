class Solution:
    def intersection(self, num1: List[int], num2: List[int]) -> List[int]:
        s1 = set(num1)
        s2 = set(num2)
        return list(s1.intersection(s2))