class Solution:
    def maxScore(self, nums: List[int]) -> int:
        def gcd(a, b):
            if b == 0:
                return a
            return gcd(b, a%b)
        n = len(nums)
        gcds = [[] for _ in range(n)]
        for i in range(n):
            for j in range(i + 1, n):
                n1, n2 = nums[i], nums[j]
                gcds[i].append((gcd(max(n1, n2), min(n1, n2)), j))
        stack = []
        self.curr = (0, [])
        self.state = 0
        self.answer = 0
        def calculate(vals):
            vals.sort()
            temp = 0
            for i, val in enumerate(vals):
                temp += ( (i + 1)* val)
            self.answer = max(self.answer, temp)
        def dfs(index):
            if index >= n - 1:
                calculate(stack.copy())
                return
            if self.state & (1 << index):
                dfs(index + 1)
                return
            for g, j in gcds[index]:
                if self.state&(1<<j) == 0:
                    self.state |= (1 << j)
                    stack.append(g)
                    dfs(index + 1)
                    stack.pop()
                    self.state ^= (1 << j)
        dfs(0)
        return self.answer
        
            