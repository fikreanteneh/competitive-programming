class Solution:
    def interpret(self, command: str) -> str:
        stack = []
        for i in command:
            if i == ")":
                first = stack.pop()
                if first == "(" : stack.append("o")
                else:
                    stack.pop()
                    stack.pop()
                    stack.append("al")
            else: stack.append(i)
        return "".join(stack)