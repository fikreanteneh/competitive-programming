class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 4:
            return max(nums)
        self.end = n - 1
        
        @functools.lru_cache(maxsize=2000)
        def solution(index):
            if index >= self.end:
                return 0
            return nums[index] + max(solution(index + 2), solution(index + 3))
        x = solution(0)
        self.end += 1
        solution.cache_clear() 
        y = solution(1)
        solution.cache_clear()
        z = solution(2)
        return max(x, y, z)