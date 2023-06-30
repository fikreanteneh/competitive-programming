class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = [num[0]]
        for i in range(1, len(num)):
            for j in range(len(stack)-1, -1, -1):
                #while k > 0 and len(stack)>0 and stack[-1] > num[i]:
                if k <= 0 or stack[-1] <= num[i]: break
                stack.pop()
                k -= 1
            stack.append(num[i])
        for i in range(k): stack.pop()
        if len(stack) == 0: stack.append("0")
        return str(int("".join(stack)))
