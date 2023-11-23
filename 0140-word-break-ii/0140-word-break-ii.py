class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordDict = set(wordDict)
        stack = []
        answer = []
        n = len(s)
        
        def solve( left ):
            if left == n:
                answer.append( " ".join(stack))
            
            for right in range(left, n):
                word = s[left: right + 1]
                
                if word in wordDict:
                    stack.append(word)
                    solve(right + 1)
                    stack.pop()        
        
        solve(0)
        return answer
        
        
        