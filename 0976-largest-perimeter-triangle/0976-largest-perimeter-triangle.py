class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        answer = 0
        sums = nums[0] + nums[1]
        for i in range(2, len(nums)):
            if sums > nums[i]: answer = max(answer, sums + nums[i])
            sums -= nums[i-2]
            sums += nums[i]
        return answer
        