class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeated = list (Counter(nums).items())
        answer = 0
        for i in repeated:
            increment = (i[1]/2) * (i[1] - 1)
            answer += (int(increment))
        return answer