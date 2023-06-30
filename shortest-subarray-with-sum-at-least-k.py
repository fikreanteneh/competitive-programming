class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        subarray = -1
        sum = 0
        i,j = 0,0
        while i < len(nums):
            sum+=nums[i]
            print(nums[i])
            while j <= i and sum >= k:
                if subarray == -1 or subarray > i-j+1: subarray = i-j + 1
                sum -= nums[j]
                j+=1
            i+=1
        return subarray
