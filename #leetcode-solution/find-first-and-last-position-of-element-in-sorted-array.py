class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        index1 = bisect_left(nums, target)
        index2 = bisect_right(nums, target)
        if index1 == index2:
            return [-1,-1]
        return [index1, index2 - 1]