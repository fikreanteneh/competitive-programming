class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        answer = []
        index = 0
        n = len(nums)
        while index < n:
            while 1 <= nums[index] <= n  and nums[index] - 1 != index:
                idx = nums[index] - 1
                temp = nums[idx]
                if temp - 1 == idx:
                    nums[index] = 0
                    break
                nums[index],  nums[idx] = nums[idx], nums[index]
            index += 1
        for i, num in enumerate(nums):
            if num-1 != i:
                return i + 1
        return n + 1