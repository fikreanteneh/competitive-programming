class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        back = 0
        front = 0
        while front < len(nums)-1:
            if len(nums) <= 1: return
            if nums[back] !=0:
                front+=1
                back+=1
            elif nums[front +1]!=0:
                if nums[front] == 0:
                    nums[front + 1], nums[back] = nums[back], nums[front + 1]
                front+=1
                back+=1
            else:
                front+=1
