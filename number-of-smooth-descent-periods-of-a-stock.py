class Solution:
    def getDescentPeriods(self, prices: List[int]) -> int:
        smooth = len(prices)
        i, j = 0, 1
        while j < len(prices):
            i = j - 1
            while j < len(prices) and prices[j-1] - prices[j] == 1:
                smooth += (j-i)
                j+=1
            j+=1
        return smooth
