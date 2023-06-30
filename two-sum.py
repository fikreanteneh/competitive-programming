class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        index = {}
        for i, num in enumerate(nums): index[num] = i
        for i ,num in enumerate(nums):
            n = target - num
            if n in index and i != index[n]: return [i, index[n]]
