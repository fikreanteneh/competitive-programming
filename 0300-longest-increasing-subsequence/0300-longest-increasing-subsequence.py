class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        
        # GreedyDP
        answer = [nums[0]]
        n = len(nums)
        for i in range(n):
            if nums[i] > answer[-1]:
                answer.append(nums[i])
            else:
                index = bisect_left(answer, nums[i])
                answer[index] = nums[i]
        
        return len(answer)
        
        
        
        
        
        # DP
        memo = [1] * len(nums)
        
        for i in range(1, len(nums)):
            maxi = 0
            for j in range(i):
                if nums[j] < nums[i]:
                    maxi = max(maxi, memo[j])
            memo[i] += maxi
        return max(memo)
                