class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        
        store = {lett: i for i, lett in enumerate(s)}
        
        stack = [""]
        
        for i, lett in enumerate(s):
            if lett in stack:
                continue
            while stack[-1] > lett and store[stack[-1]] > i:
                stack.pop()
            stack.append(lett)
        
        return "".join(stack)
                