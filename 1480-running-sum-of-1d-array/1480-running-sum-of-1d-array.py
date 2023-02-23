class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sums = 0
        for i, num in enumerate(nums):
            sums += num
            nums[i] = sums
        return nums