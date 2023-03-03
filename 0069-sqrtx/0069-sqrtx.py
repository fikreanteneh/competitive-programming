class Solution:
    def mySqrt(self, x: int) -> int:
        low, high = 0, x
        
        while low <= high:
            mid = low + ((high - low) // 2)
            square = mid * mid
            if square == x:
                return mid
            elif square < x:
                if (mid + 1)  *  (mid + 1) > x:
                    return mid
                low = mid + 1
            else:
                if (mid - 1)  *  (mid - 1) < x:
                    return mid - 1
                high = mid - 1 
            
            
        