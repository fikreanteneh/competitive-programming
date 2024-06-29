class Solution:
    def partition(self, s: str) -> List[List[str]]:
        
        def check(string):
            return string == string[::-1]
        
        n = len(s)
        answer = []
        stack = []
        def backtrack(index):
            if index == n:
                answer.append(stack[:])
            
            for i in range(index + 1, n + 1):
                subString = s[index : i]
                if not check(subString):
                    continue
                stack.append(subString)
                backtrack(i)
                stack.pop()
        
        backtrack(0)
        return answer