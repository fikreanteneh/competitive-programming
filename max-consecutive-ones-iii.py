class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        back = 0
        front = 0
        length = len(nums)
        count = 0
        maxLen = 0 
        while front < length:
            if nums[front]==0:
                count +=1
            while  count > k:
                if (nums[back] == 0):
                    count-=1
                back+=1
            maxLen = max(maxLen, front-back + 1)         
            front += 1
        return maxLen
