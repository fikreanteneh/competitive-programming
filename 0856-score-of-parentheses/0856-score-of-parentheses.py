class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [[0, "add"]]
        for i, par in enumerate(s):
            if par == "(":
                stack.append(False)
                continue
            appended = [0,"add"]
            while stack[-1]: 
                appended[0] += stack[-1][0]
                stack.pop()
            stack.pop()
            if not appended[0]: 
                appended[0] += 1
            else:
                appended[0] *= 2
            stack.append(appended)
        ans = 0
        for i in stack:
            ans += i[0]
        return ans
   # (((())))
# 0 1 2 
# 1
# 1



