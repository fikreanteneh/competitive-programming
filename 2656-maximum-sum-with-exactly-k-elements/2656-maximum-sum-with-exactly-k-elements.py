class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        maxi = 0
        for val in nums:
            maxi = max(maxi, val)
        ans = 0
        for i in range(k):
            ans += (maxi + i)
            # print(maxi + i)
        return ans