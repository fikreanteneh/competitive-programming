class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxi = 0
        n = len(s)
        store = [0] * 26
        indexMax = 0
        j = 0
        for i,lett in enumerate(s):
            store[ord(lett)-65] += 1
            maximum = max(store)
            while i - j - maximum + 1 > k:
                
                store[ord(s[j])-65] -= 1
                j += 1
                maximum = max(store)
            maxi = max(maxi, i - j + 1)
        return maxi