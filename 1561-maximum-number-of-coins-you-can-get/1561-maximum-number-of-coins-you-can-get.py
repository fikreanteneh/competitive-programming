class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        maxi = 0
        piles.sort()
        x = len(piles)// 3
        for i in range(len(piles)-2, x-1, -2) : maxi += piles[i]
        return maxi