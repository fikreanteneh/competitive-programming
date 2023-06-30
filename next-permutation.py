class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = True
        for i in range(len(nums)-2, -1, -1):
            if nums[i] < nums[i+1]:
                flag = False
                break
        if flag:
            nums[0:len(nums)] = reversed(nums[0:len(nums)])
            return
        
        for j in range(len(nums)-1, -1, -1):
            if nums[j]> nums[i]: break
        nums[i], nums[j] = nums[j], nums[i]
        nums[i+1:len(nums)] = reversed(nums[i+1:len(nums)])
