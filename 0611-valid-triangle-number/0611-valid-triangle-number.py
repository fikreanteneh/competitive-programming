class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        if n < 3:
            return 0
        answer = 0
        for i in range(n):
            for j in range(i + 1, n):
                sums = nums[i] + nums[j]
                index = bisect_left(nums, sums)
                answer += max(0, index - j - 1)
        return answer