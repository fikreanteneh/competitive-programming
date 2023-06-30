class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = max(weights), sum(weights)
        
        while low <= high:
            mid = low + (high - low) //2
            day = 0
            sums = 0
            for weight in weights:
                sums += weight
                if sums == mid:
                    day += 1
                    sums = 0
                elif sums > mid:
                    day += 1
                    sums = weight
            if sums:
                day += 1
            if day > days:
                low = mid + 1
            else:
                high = mid - 1
        
        return low