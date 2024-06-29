class Solution:
    def checkPartitioning(self, s: str) -> bool:
        def check(string):
            return string == string[::-1]
        
        n = len(s)
        def backtrack(index, div):
            if index == n:
                return div == 3
            if div == 2:
                return check(s[index:])
            if div >= 3:
                return False
            
            for i in range(index + 1, n + 1):
                subString = s[index : i]
                if check(subString) and backtrack(i, div + 1):
                    return True
            return False
                
        
        return backtrack(0, 0)
