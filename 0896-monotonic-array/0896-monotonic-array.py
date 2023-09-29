class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n = len(nums)
        if n <= 2:
            return True
        curr = nums[0]
        for i in range(1, n):
            curr, nums[i] = nums[i], nums[i] - curr
        maxi, mini = float("-inf"), float("inf")
        for i in range(1, n):
            maxi = max(maxi, nums[i])
            mini = min(mini, nums[i])
        
        return (maxi <= 0 and mini <=0) or (maxi >= 0 and mini >= 0)