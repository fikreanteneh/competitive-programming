class Solution:
    def countVowels(self, word: str) -> int:
        n = len(word)
        sum = 0
        for i, letter in enumerate(word):
            if letter in "aeiou":
                sum += ((i + 1) * (n - i))
        return sum
