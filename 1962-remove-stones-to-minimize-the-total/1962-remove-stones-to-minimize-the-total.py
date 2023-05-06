class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        for i, val in enumerate(piles):
            piles[i] = -1 * val
        heapify(piles)
        
        for _ in range(k):
            heappush(piles, floor( heappop(piles)/2))
        
        return -1 * sum(piles)
            
        