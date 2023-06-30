class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i, val in enumerate(stones):
            stones[i] = val * -1
        heapify(stones)
        while len(stones) > 1:
            y = heappop(stones)
            x = heappop(stones)
            if y - x:
                heappush(stones, y - x)
        stones.append(0)
        return -1 * stones[0]
        