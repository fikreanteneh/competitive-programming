class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        ans = 0
        for i, val in enumerate(word):
            if val in "aeiou":
                ans += ( (i-(-1))*(n - i) )
        return ans