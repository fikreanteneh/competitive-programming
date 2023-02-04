class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        for i, diff in enumerate(difficulty):
            difficulty[i] = (diff, profit[i])
        difficulty.sort()
        worker.sort()
        ans = 0
        i = 0
        maxi = 0
        n = len(difficulty)
        for work in (worker):
            while i < n and work >= difficulty[i][0]:
                maxi = max(maxi, difficulty[i][1])
                i += 1
            ans += maxi
        return ans