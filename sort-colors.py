class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        new = [[],[],[]]
        for i in range (len(nums)):
            new[nums[i]].append(i)
        new = new[0] + new[1] + new[2]
        print(new)
        x = []
        for i in new:
            x.append(nums[i])
        for i in range (len(x)):
            nums[i] = x[i]
        
