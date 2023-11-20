class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        forward = [0]*n
        backward = [0]*n
        last1 = float("inf")
        last2 = float("-inf")
        curr = 0
        for i, val in enumerate(prices):
            if val < last1:
                last1 = last2 = val
            elif val > last2:
                last2 = val
                curr = max(curr, last2 - last1)
            forward[i] = curr
        last1 = float("-inf")
        last2 = float("inf")
        curr = 0
        for i in range(n - 1, -1, -1):
            val = prices[i]
            if val > last1:
                last1 = last2 = val
            elif val < last2:
                last2 = val
                curr = max(curr, last1 - last2)
            backward[i] = curr
        ans = 0
        for x, y in zip(forward, backward):
            ans = max(ans, x + y)
        return ans
        