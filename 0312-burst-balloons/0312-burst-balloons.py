class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        
        nums = [1] + nums + [1]
        @cache
        def solution(left, right):
            if right - left == 0:
                return 0
            answer = 0
            for i in range(left + 1, right):
                ans = nums[left] * nums[i] * nums[right]
                leftSide = solution(left, i)
                rightSide = solution(i, right)
                answer = max(answer, leftSide + rightSide + ans)
            return answer
                
        return solution(0, len(nums) - 1)
            
        
        # answer = 0
        # while nums:
        #     mini = min(nums)
        #     print(mini)
        #     index = nums.index(mini)
        #     left = 1 if index == 0 else nums[index - 1]
        #     right = 1 if index == len(nums) - 1 else nums[index + 1]
        #     answer += left * right * mini
        #     nums.pop(index)
        # return answer
            