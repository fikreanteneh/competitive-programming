class Solution:
    def findGCD(self, nums: List[int]) -> int:
        x = min(nums)
        y = max(nums)
        
        while True:
            temp = y % x
            if not temp:
                return x
            y, x = x, temp
        
#         def euclid(y, x):
            
#             return euclid(x, temp)
        
#         return euclid(y, x)