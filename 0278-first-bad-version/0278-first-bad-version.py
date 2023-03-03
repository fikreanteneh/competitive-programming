# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left, right = 1, n
        while left <= right: 
            mid = left + ((right - left) // 2) 
            if isBadVersion(mid): 
                if mid == 1 or not isBadVersion(mid - 1): 
                    return mid 
                right = mid - 1 
            else: 
                if isBadVersion(mid+1): 
                    return mid + 1
                left = mid + 1 


 