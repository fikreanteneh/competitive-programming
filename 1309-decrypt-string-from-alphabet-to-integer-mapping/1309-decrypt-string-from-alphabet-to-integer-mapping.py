class Solution:
    def freqAlphabets(self, s: str) -> str:
        stack = []
        for i in s:
            if i == "#":
                second = stack.pop()
                first = stack.pop()
                stack.append(first + second)
            else: stack.append(i)
        for i in range (len(stack)):
            stack[i] = chr(int(stack[i]) + 96)
        return "".join(stack)