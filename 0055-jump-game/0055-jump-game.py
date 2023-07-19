class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # store = set()
        n = len(nums) - 1
        @cache
        def sol(index):
            if index == n:
                return True
            for i in range(1,nums[index] + 1):
                if sol(index + i):
                    return True
            return False
        
        return sol(0)