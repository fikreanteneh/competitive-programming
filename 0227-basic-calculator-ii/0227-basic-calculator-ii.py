class Solution:
    def calculate(self, s: str) -> int:
        values  = []
        i = 0
        for j in range(len(s)):
            num = s[j]
            if num in "+-*/":
                values.append(int(s[i:j]))
                i = j + 1
                values.append(num)
        values.append(int(s[i:j+1]))
        stack = []
        i = 0
        while i < len(values):
            val = values[i]
            if type(val) == str and val in "*":
                stack.append(stack.pop() * values[ i + 1])
                i += 1
            elif  type(val) == str and val in "/":
                stack.append(stack.pop() // values[ i + 1])
                i += 1
            else: stack.append(val)
            i += 1
        values, stack, i = stack, [], 0
        while i < len(values):
            val = values[i]
            if  type(val) == str and val in "+":
                stack.append(stack.pop() + values[ i + 1])
                i += 1
            elif  type(val) == str and val in "-":
                stack.append(stack.pop() - values[ i + 1])
                i += 1
            else: stack.append(val)
            i += 1
        return stack[-1]