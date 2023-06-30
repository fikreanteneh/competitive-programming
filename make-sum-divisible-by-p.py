class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        prefix = {0:-1}
        x = sum(nums) % p
        if x == 0: return 0
        sums, ans = 0, float("inf")
        for i,num in enumerate(nums):
            sums = (sums + num) % p
            prefix[sums] = i
            if (sums - x) % p in prefix: ans = min(ans, i - prefix[(sums - x) % p])
        return ans if ans < i + 1 else -1
