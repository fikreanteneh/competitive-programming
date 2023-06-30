class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix, sums, ans = {0:1}, 0, 0
        for i in nums:
            sums += i
            x = sums % k
            ans += (prefix.get(x, 0))
            prefix[x] = prefix.get(x, 0) + 1
        return ans