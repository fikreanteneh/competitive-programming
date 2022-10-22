class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            if not stack or (stack[-1]> 0 and i > 0) or (stack[-1] < 0 and i < 0) or (stack[-1] < 0 and i > 0): stack.append(i)
            elif abs(stack[-1]) == abs(i):  stack.pop()
            else:
                while stack and abs(stack[-1]) < abs(i) and ((stack[-1] < 0 and i > 0) or (stack[-1] > 0 and i < 0)): stack.pop()
                if stack and 0 - stack[-1] == i: stack.pop()
                elif not stack: stack.append(i)
                elif (stack[-1] < 0 and i < 0) or (stack[-1] > 0 and i > 0): stack.append(i)
        return stack
