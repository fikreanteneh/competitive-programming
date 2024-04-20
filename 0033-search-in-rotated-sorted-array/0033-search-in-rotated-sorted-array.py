class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        def getRotatedIndex():
            left, right = 0, n - 1
            while left < right:
                mid = (left + right) // 2
                if nums[mid - 1] > nums[mid] < nums[ (mid + 1)% n]:
                    return mid
                elif nums[mid] > nums[right]:
                    left = mid + 1
                else:
                    right = mid
            return left
        def getIndex(start):
            left, right = start, start + n - 1
            while left <= right:
                mid = (left + right) // 2
                if nums[mid % n] == target:
                    return mid % n
                elif nums[mid % n] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return -1
        start = getRotatedIndex()
        return getIndex(start)
            