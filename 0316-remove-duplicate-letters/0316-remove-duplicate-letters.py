class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last = {lett: i for i, lett in enumerate(s)} 
        stack = [""]
        pushed = set()
        for i, lett in enumerate(s):
            if lett not in pushed:
                while stack[-1] > lett and last[stack[-1]] > i:
                    pushed.remove(stack.pop())
                stack.append(lett)
                pushed.add(lett)
            
        return "".join(stack)