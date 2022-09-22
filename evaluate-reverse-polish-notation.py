class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            if i == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)
            elif i == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)
            elif i == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)
            elif i == "/":
                x = stack.pop()
                y = stack.pop()
                z = y//x
                if z <0: z = 0
                stack.append(z)
            else: stack.append(int(i))
        return stack[0]
