class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        t = s[::-1]
        
        store = [ [0 for _ in range(n + 1) ] for _ in range(n + 1)]
        answer = (0, 0, 0)
        for i in range(n - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    store[i][j] = store[i + 1][j + 1] + 1
                    # print(i, j, store[i][j])
                    if store[i][j] > answer[0] and ( i == (n - 1) -  (j + store[i][j] - 1)   ) :
                        answer = (store[i][j], i, i+store[i][j])
        return s[answer[1]:answer[2]]
                    
                