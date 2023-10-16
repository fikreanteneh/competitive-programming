class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:
        n = len(nums)
        result = nums[0]
        for val in nums:
            result &= val
        if result != 0:
            return 1
        curr = (1 << 22) - 1
        answer = 0
        for num in nums:
            curr &= num
            if curr == 0:
                answer += 1
                curr = (1 << 22) - 1
        return answer
                
                
            