class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2
        type = len(set(candyType))
        return min(n, type)