class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        subarr = 0
        sum = 0
        cache = {0:1}
        for i in range(len(nums)):
            sum += nums[i]
            if sum - k in cache:
                subarr += cache[sum - k]
            if sum in cache: cache[sum] += 1
            else: cache[sum] =  1
            
        return subarr
