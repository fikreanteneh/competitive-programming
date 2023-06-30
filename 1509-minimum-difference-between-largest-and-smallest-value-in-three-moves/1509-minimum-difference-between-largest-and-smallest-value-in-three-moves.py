class Solution:
    def minDifference(self, nums: List[int]) -> int:
        if len(nums) <= 4:
            return 0
        nums.sort()
        ans = float("inf")

        for i in range(4):
            ans = min(ans, abs(nums[i] - nums[i - 4]))
        return ans