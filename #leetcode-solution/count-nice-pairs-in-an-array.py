class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        store = defaultdict(int)
        MOD = 10**9 + 7
        ans = 0
        for i, num in enumerate(nums):
            rev = int(str(num)[::-1])
            ans += store[num - rev]
            ans %= MOD
            store[num - rev] += 1  
        return ans
         