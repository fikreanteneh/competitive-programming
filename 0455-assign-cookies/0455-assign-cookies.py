class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        n = len(g)
        m = len(s)
        ans = 0
        i, j = 0, 0
        while i < n and j < m:
            while j < m and s[j] < g[i]:
                j += 1
            
            if j < m :
                ans += 1
            
            i += 1
            j += 1
        return ans
                