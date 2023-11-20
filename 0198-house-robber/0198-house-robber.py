class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        store = [None]*n
        sums = nums.copy()
        for i in range(n):
            curr = (0, None)
            val = nums[i]
            for j in range(i - 2, -1, -1):
                if sums[j] >= curr[0]:
                    curr = (sums[j], j)
            store[i] = curr[1]
            sums[i] += curr[0]
        answer = []
        start = n - 1 if sums[n - 1] > sums[n - 2] else n - 2
        while start is not None:
            answer.append(start)
            start = store[start]
        ans = 0
        for i in answer:
            ans += nums[i]
        return ans
            
                