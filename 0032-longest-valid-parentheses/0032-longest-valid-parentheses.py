class Solution:
    def longestValidParentheses(self, s: str) -> int:
        
        stack = []
        ans = [0] * len(s)
        
        for i, val in enumerate(s):
            if val == ")":
                if not stack:
                    ans[i] = 0
                else:
                    ans[stack.pop()] = 1
                    ans[i] = 1
            else:
                stack.append(i)
        
        maxi = 0
        sums = 0
        for i in ans:
            sums *= i
            sums += i
            maxi = max(sums, maxi)
        return maxi