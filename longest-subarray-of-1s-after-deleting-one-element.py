class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maximum = 0
        last0 = None
        i,j,k = -1, -1, 0
        flag = True
        for k in range(len(nums)):
            if nums[k] == 0:
                flag = False
                i = j + 1
                j = k
            maximum = max(maximum, k-i)
        if flag: maximum -= 1
        return maximum
            
        
