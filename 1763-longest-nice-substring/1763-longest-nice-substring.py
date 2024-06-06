class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        def solve(left, right):
            if left > right:
                return ""
            check = { s[i] for i in range(left, right + 1)}
            for i in range(left, right + 1):
                lett = s[i]
                if lett.swapcase() not in check:
                    s1 = solve(left, i - 1) 
                    s2 = solve(i + 1, right)
                    
                    if len(s1) < len(s2):
                        return s2
                    return s1
            
            return s[left:right + 1]   
        
        return solve(0, len(s) - 1)