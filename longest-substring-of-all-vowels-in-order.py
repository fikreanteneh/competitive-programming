class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        i = j = ans = 0
        n = len(word)
        while j < n:
            j += 1
            if word[i] != "a": 
                i = j
                continue
            vowel = ["a"]
            while j < n and word[j] in "aeiou" and word[j] >= vowel[-1]:
                if vowel[-1] != word[j]: vowel.append(word[j])
                j += 1
            if len(vowel) == 5: ans = max(ans, j - i)
            i = j
        return ans
