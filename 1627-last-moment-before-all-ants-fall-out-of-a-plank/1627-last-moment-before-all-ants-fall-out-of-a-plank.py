class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        answer = 0
        for val in left:
            answer = max(answer, val)
        for val in right:
            answer = max(answer, n - val)
        return answer