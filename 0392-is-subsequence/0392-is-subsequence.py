class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        i, j = 0, 0
        n, m = len(s), len(t)
        while i < n:
            while j < m and s[i] != t[j]:
                j += 1
            if j >= m: break
            j += 1
            i += 1
        return i == n
        