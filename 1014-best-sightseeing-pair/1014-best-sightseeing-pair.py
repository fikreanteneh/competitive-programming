class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        maxi = 0
        curr = values[-1] - 1
        for i in range(len(values) - 2, -1, -1):
            maxi = max(maxi, values[i] + curr)
            curr = max(curr - 1, values[i] - 1)
        return maxi