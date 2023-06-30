class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        prefix = {}
        count = 0
        for i in range (len(nums)):
            num = k - nums[i]
            if num in prefix and prefix[num] > 0: 
                prefix[num]-=1
                count += 1
            elif nums[i] in prefix : prefix[nums[i]] += 1
            else: prefix[nums[i]] = 1
        return count
                
