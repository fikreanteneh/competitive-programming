class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        x = ''
        for i in s:
            if i == "(":
                stack.append(x)
                x = ''
            elif i == ")":
                x = stack.pop() + x[::-1]
            else:
                x+=i
        return x
