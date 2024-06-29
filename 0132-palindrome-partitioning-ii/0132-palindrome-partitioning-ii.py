class Solution:
    def minCut(self, s: str) -> int:
        def check(string):
            return string == string[::-1]
        store = [float("inf") for _ in range(len(s) + 1)]
        store[-1] = -1
        for i in range(len(s)):
            minimum = float("inf")
            for j in range(i + 1):
                subString = s[j : i + 1]
                if not check(subString):
                    continue
                minimum = min(minimum, store[j - 1] + 1)
            store[i] = minimum
                
        return store[-2]
                