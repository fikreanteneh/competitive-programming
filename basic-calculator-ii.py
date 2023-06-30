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
        """stack, j, i = [], 0, 0
        while j < len(s):
            num = s[j]
            now = s[i:j]
            if num in "*/":
                now = s[i:j]
                i = j + 1
                while s[j].isnumeric(): j +=1
                if num == "*" : stack.append(int(now) * int(s[i:j]))
                else: stack.append(int(now) // int(s[i:j]))
                j += 1
            elif num in "+-":
                num = int(s[i:j])
                i = j
            stack.append(num) 
            j += 1
        return sum(stack)"""
        
            
