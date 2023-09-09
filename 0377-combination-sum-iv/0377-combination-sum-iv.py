class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        answer = [0] * (target + 1)
        answer[0] = 1
        
        for tar in range(1, target + 1):
            for num in nums:
                if tar - num >= 0 and answer[tar - num] > 0:
                    answer[tar] += answer[tar - num]
            
        return answer[target]
            