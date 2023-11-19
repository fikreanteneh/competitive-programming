class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        left, right = 0, 0
        ans = 0
        while left < n:
            right = left + 1
            while right < n and nums[right] == nums[left]:
                right += 1
            
            ans += (n - right)
            left = right
        return ans