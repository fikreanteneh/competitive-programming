class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        store = [0] * 26
        sums = 0
        i = j = 0
        length = 0
        while j < len(s):
            let = s[j]
            store[ord(let)-65] += 1
            maxi = max(store)
            sums = sum(store) - maxi
            if sums <= k: length = max(length, j - i + 1)
            while sums > k:
                store[ord(s[i])-65]-=1
                maxi = max(store)
                sums = sum(store) - maxi
                i += 1
            j += 1
        return length
                
