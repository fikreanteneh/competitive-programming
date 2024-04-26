class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        @cache
        def solve(index1, index2):
            if index1 == n and index2 == m:
                return 0
            if index2 == m:
                return solve(index1 + 1, index2) + 1
            if index1 == n:
                return solve(index1, index2 + 1) + 1
                
                
            forInsert = solve(index1, index2 + 1) + 1   
            forDelete = solve(index1 + 1, index2) + 1
            forReplace = solve(index1 + 1, index2 + 1) + 1
            
            if word1[index1] == word2[index2]:
                forReplace -= 1
                
            return min(forInsert, forDelete, forReplace)
        
        return solve(0,0)
            