class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack_array= []
        for i in tokens:
            if i == "+":
                stack_array.append(stack_array.pop() + stack_array.pop())

            elif i == "*":
                stack_array.append(stack_array.pop() * stack_array.pop())

            elif i == "-":
                a =  stack_array.pop()
                b = stack_array.pop()
                stack_array.append(b-a)
            elif i == "/":
                a =  stack_array.pop()
                b = stack_array.pop()
                stack_array.append(int(b/a))
            else: 
                stack_array.append(int(i))
        return stack_array[0]
