class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        target = sum(nums)/2
        n = len(nums)
        @cache
        def solve(index, currentSum):
            if index >= n or currentSum > target:
                return False
            if currentSum == target:
                return True
            
            return solve(index + 1, currentSum + nums[index]) or solve(index + 1, currentSum)
        
        return solve(0, 0)
            