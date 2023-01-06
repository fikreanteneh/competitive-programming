class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexes = {}
        for i, num in enumerate(nums):
            indexes[num] = i
        for i in operations:
            index = indexes[i[0]]
            del indexes[i[0]]
            indexes[i[1]] = index
            nums[index] = i[1]
        return nums