class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i]%2 != 0: nums[i] = 1
            else: nums[i] = 0
        cache = {0:1}
        sum = 0
        count = 0
        for i in range(len(nums)):
            sum += nums[i]
            if sum-k in cache: count += cache[sum-k]
            if sum in cache: cache[sum] += 1
            else: cache[sum] =  1
        return count
            
