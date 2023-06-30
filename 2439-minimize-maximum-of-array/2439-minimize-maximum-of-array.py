class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        runningSum, answer = 0, 0
        
        for i, val in enumerate(nums):
            runningSum += val
            answer = max(answer, ceil(runningSum/ (i + 1)))
            
        return answer