class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        low, high = 1, max(piles)
        mini = float("inf")
        
        while low <= high:
            mid = low + (high - low) // 2
            time = 0
            for i in piles:
                if mid >= i:
                    time+= 1
                else:
                    time += (ceil(i / mid))
            if time <= h:
                mini = min(mini, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        
        return mini
                
                
            
            