class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def check(string):
            return string == string[::-1]
        store = [[] for _ in range(len(s) + 1)]
        store[-1].append([])
        for i in range(len(s)):
            subStrings = []
            for j in range(i + 1):
                subString = s[j : i + 1]
                if not check(subString):
                    continue
                for subStrings in store[j - 1]:
                    store[i].append( subStrings + [subString] )
        return store[-2]
                
        
        
        
        
        
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