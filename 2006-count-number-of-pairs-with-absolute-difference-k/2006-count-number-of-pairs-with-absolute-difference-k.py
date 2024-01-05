class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        count = Counter(nums)
        ans = 0
        for i in nums:
            ans += count[i - k]
            ans += count[i + k]
            count[i] -= 1
        return ans