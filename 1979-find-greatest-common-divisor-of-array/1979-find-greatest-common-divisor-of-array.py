class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x = min(nums)
        y = max(nums)
        
        def euclid(y, x):
            temp = y % x
            if not temp:
                return x
            return euclid(x, temp)
        
        return euclid(y, x)