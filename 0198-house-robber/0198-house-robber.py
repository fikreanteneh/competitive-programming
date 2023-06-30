class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {}
        
        
        def calc(house):
            if house >= n:
                return 0
            
            if house not in memo:
                x = calc(house + 2)
                y = calc(house + 3)
                memo[house] = max(x + nums[house], y + nums[house])
                
            return memo[house]
        
        return max(calc(0), calc(1))