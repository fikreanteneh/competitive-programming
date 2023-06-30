class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums)
        for i in range(n-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i] * 2
                nums[i+1] = 0
        if len(nums) <= 1: 
            return nums
        back = 0
        front = 0
        while front < len(nums)-1:
            if nums[back] !=0:
                back+=1
            elif nums[front + 1] != 0:
                if nums[front] == 0:
                    nums[front + 1], nums[back] = nums[back], nums[front + 1]
                back+=1
            front+=1
        return nums
                