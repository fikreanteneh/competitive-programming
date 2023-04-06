class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        stack = []
        n = len(nums)
        self.cur = 0
        check = 2 ** (n) - 1
        
        def solution():
            if self.cur == check:
                ans.append(stack.copy())
                return
            for i in range(0, n ):
                if not (self.cur & ( 1 << i)):
                    stack.append(nums[i])
                    self.cur |= (1 << i)
                    solution()
                    self.cur ^= (1 << i) 
                    stack.pop()
        solution()
        return ans