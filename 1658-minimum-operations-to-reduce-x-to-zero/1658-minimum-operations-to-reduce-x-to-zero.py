class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)
        answer = -1
        sums = 0
        i, j = 0, 0
        for i in range(n):
            while j < n and sums < target:
                sums += nums[j]
                j += 1
            if sums == target:
                answer = max(answer, (j - i))
            sums -= nums[i]
            i += 1
        return n - answer if answer > -1 else -1
                