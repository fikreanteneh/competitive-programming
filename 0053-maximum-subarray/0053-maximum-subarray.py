class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)
        i = j = sums = maxi = 0
        while  j < n:
            cur = sums + nums[j]
            while cur < 0 and i <= j:
                cur -= nums[i]
                i += 1
            sums = cur
            maxi = max(maxi, sums)
            j += 1
        if maxi == 0: return max(nums)
        return maxi
            
            