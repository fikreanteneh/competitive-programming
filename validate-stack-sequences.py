class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        ind = 0
        stack = []
        for i in pushed:
            stack.append(i)
            while len(stack)!= 0 and stack[-1] == popped[ind]:
                if ind >= len(popped): break
                ind+=1
                stack.pop()
        if ind == len(popped): return True
        return False
