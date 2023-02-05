class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        for i, num in enumerate(nums):
            if nums[i] == val:
                nums[i] = "_"
        i = len(nums) - 1
        while i >= 0:
            if nums[i] == "_":
                nums.pop(i)
            i -= 1
        return len(nums)
                
                
                