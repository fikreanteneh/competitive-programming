class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        self.ans = float("inf")
        self.n = len(nums)
        @cache
        def dfs(i, k):
            if k == 1:
                return sum(nums[i:])
            runSum = nums[i]
            mini = float("inf")
            for nextt in range(i + 1, self.n - k + 2):
                prev = dfs(nextt, k - 1)
                mini = min(mini, max( runSum, prev ))
                runSum += nums[nextt]
            return mini
                           
        return dfs(0, k)
