class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        sum = 0
        for i in range(k): sum += cardPoints[i]
        maximum = sum
        for i in range(k):
            sum = sum - cardPoints[k-i-1] + cardPoints[-1-i]
            maximum = max(maximum, sum)
        return maximum
