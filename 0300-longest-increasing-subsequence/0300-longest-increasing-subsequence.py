class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [1] * len(nums)
        
        for i in range(1, len(nums)):
            maxi = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxi = max(maxi, memo[j])
            memo[i] += maxi
        return max(memo)
                