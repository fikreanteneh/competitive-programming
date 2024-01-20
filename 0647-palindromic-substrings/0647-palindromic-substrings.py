class Solution:
    def countSubstrings(self, s: str) -> int:
        s+= "-"
        possible = []
        answer = 0
        for i in range(len(s) - 1):
            char = s[i]
            answer += 1
            new = [i, i - 1]
            for p in possible:
                if s[p] == char:
                    answer += 1
                    new.append( p - 1)
            
            possible = new
        return answer
                    
            