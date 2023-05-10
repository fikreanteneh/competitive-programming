class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        prev = []
        n = len(heights)
        for i in range(1, n):
            # print(prev)
            
            diff = heights[i] - heights[i - 1]
            if diff <= 0:
                continue
            if not ladders and not bricks:
                return i - 1
            
            
            heappush(prev, diff)
            if ladders:
                ladders -= 1
            else:
                x = heappop(prev)
                if x > bricks:
                    return i - 1
                bricks -= x
            
        
        return n - 1