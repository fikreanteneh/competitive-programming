class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def value(s):
            stack = []
            for i in s:
                if i == "#":
                    if stack:
                        stack.pop()
                    continue
                stack.append(i)
            return stack
        
        return value(s) == value(t)