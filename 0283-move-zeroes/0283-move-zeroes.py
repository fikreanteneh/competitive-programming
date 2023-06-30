class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        if n <= 1: return
        back = 0
        front = 0
        while front < n:
            if nums[front] != 0:
                nums[front], nums[back] = nums[back], nums[front]
                back += 1
            front += 1
        
        