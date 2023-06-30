class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
            stack = []
            for i in num:        
                while  k > 0 and stack and stack[-1] > i:
                    stack.pop()
                    k -= 1
                stack.append(i)
            while k > 0 and stack:
                stack.pop()
                k -= 1
            if not stack:
                return "0"
            return str(int("".join(stack)))