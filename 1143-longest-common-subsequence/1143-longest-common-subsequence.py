class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        
        n = len(text1)
        m = len(text2)
        store = [[0 for i in range(n + 1)] for j in range(m + 1)]
        
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if text2[i] == text1[j]:
                    store[i][j] = 1 + store[i + 1][j + 1]
                else:
                    store[i][j] = max(store[i][j + 1], store[i + 1][j])
        return store[0][0]
                