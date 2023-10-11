class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        left, right = min(nums), max(nums)
        nums = sorted(set(nums))
        
        ans = float("inf")
        for i, start in enumerate(nums):
            end = start + n - 1
            index = bisect_right(nums, end)
            ans = min(ans, n - (index - i) )
        return ans