class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        sums = 0
        answer = 0
        for i in nums:
            sums += i
            answer = max(answer, sums)
            if i == 0:
                sums = 0
        return answer