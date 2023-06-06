class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}
        n = len(nums)
        
        @cache
        def solution(curr, index):
            if index == n:
                return 1 if curr == target else 0
            answer = 0
            answer += solution(curr + nums[index], index + 1)
            answer += solution(curr - nums[index], index + 1) 
            return answer
        
        return solution(0, 0)