class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [[0, "add"]]
        for i, par in enumerate(s):
            if par == "(":
                stack.append(False)
            else:
                if not stack[-1]:
                    stack.pop()
                    stack.append([1,"add"])
                else:
                    sums = 0
                    while stack[-1] and stack[-2]: 
                        stack[-2][0] += stack[-1][0]
                        stack.pop()
                    y = stack.pop()
                    stack.pop()
                    stack.append([y[0] * 2, "add"])
            # print(stack)  
        ans = 0
        for i in stack:
            ans += i[0]
        return ans
   
# 0 1 2 
# 1
# 1



