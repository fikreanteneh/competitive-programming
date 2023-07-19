class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # store = set()
        n = len(nums) - 1
        last = n
        for i in range(n - 1, -1, -1):
            if nums[i] + i >= last:
                last = i
        return last <= 0