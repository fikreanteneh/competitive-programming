class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        nums.sort()
        n = len(nums)
        count = [0] * (n + 1)
        
        for i in requests:
            count[i[0]] += 1
            count[i[1] + 1] -= 1
        count.pop()
        sums = 0
        for i, num in enumerate(count):
            sums += num
            count[i] = sums
        count.sort()
        ans = 0
        for i, j in zip(reversed(count),reversed(nums)):
            ans += (i * j)
        return ans % (10**9 + 7 ) 
        