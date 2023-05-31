class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        answer = [0] * (target + 1)
        answer[0] = 1
        
        for i in range(1, target + 1):
            temp = 0
            for j in nums:
                if i - j >= 0 and answer[i - j] >= 0:
                    temp += answer[i - j]
            answer[i] = temp
        return answer[target]
            