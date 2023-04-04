class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxi = 0
        for i in nums: 
            maxi|= i
        track = 0
        n = len(nums)
        self.answer = 0
        def solution(index, curr):
            
            for i in range(index, n):
                new = curr | nums[i]
                if new == maxi:
                    self.answer += 1
                solution(i + 1, new)
                    
        solution(0, 0)
        return self.answer
