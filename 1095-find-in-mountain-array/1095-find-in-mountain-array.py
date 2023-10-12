# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountain: 'MountainArray') -> int:
        n =  mountain.length()
        left, right = 0, n-1
        while left <= right:
            mid = (left + right) // 2
            lefter = mountain.get(mid - 1) if mid > 0 else float("-inf")
            midder = mountain.get(mid)
            righter = mountain.get(mid + 1) if mid < n - 1 else float("-inf")
            if lefter < midder > righter:
                break
            elif lefter < midder < righter:
                left = mid + 1
            else:
                right = mid - 1
        def leftCheck(left, right, target):
            while left <= right:
                mid = (left + right) // 2
                midder = mountain.get(mid)
                if midder == target:
                    return mid
                elif midder > target:
                    right = mid - 1
                else:
                    left = mid + 1
        def rightCheck(left, right ,target):
            while left <= right:
                mid = (left + right) // 2
                midder = mountain.get(mid)
                if midder == target:
                    return mid
                elif midder < target:
                    right = mid - 1
                else:
                    left = mid + 1
        case1 = leftCheck(0, mid, target)
        case2 = rightCheck(mid, n - 1, target)
        if case1 is not None: return case1
        elif case2 is not None: return case2
        return -1
            