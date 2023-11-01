class Solution:
    def soupServings(self, n: int) -> float:
        if n > 5000:
            return 1
        operation = [ (100, 0), (75, 25), (50, 50), (25, 75) ]
        @cache
        def dfs(n, m):
            if n == 0 and m == 0:
                return 0.5
            if n == 0:
                return 1
            if m == 0:
                return 0
            answer = 0
            for x, y in operation:
                answer += dfs( n - min(n, x), m - min(m, y) )
            return 0.25*answer
        return dfs(n, n)