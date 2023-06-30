class Solution:
    def subarraysWithKDistinct(self, nums: List[int], k: int) -> int:
        return self.atmost(nums, k) - self.atmost(nums, k-1)
    
    def atmost(self, nums, k):
        count = defaultdict(int)
        n = len(nums)
        left = right = ans = 0
        for right in range(n):
            count[nums[right]] += 1
            while left <= right and len(count) > k:
                count[nums[left]] -= 1
                if count[nums[left]] == 0:
                    count.pop(nums[left])
                left += 1
            ans += (right - left + 1)
        return ans
        