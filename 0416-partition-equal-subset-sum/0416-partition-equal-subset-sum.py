class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        sums = sum(nums)
        if sums%2 == 1:
            return False
        
        @cache
        def solve(index, target):
            if target == 0:
                return True
            if target < 0 or index >= n:
                return False
            return solve(index + 1, target - nums[index]) or solve(index + 1, target)
        
        return solve(0, sum(nums)/2)