class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        stack = []
        n = len(nums)
        self.cur = 0
        
        def solution(index):
            if index == n:
                ans.append(stack.copy())
                return
            for i in range(0, n ):
                if not (self.cur & ( 1 << i)):
                    stack.append(nums[i])
                    self.cur |= (1 << i)
                    solution(index + 1)
                    self.cur ^= (1 << i) 
                    stack.pop()
        solution(0)
        return ans