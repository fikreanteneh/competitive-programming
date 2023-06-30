class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = j = sum = 0
        size = inf
        
        while j < len(nums):
            sum += nums[j]
            while sum >= target:
                size = min (size, j - i + 1)
                sum -= nums[i]
                i += 1
            j+=1
        if size == inf: size = 0
        return size
