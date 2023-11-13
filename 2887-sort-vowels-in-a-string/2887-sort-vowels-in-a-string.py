class Solution:
    def sortVowels(self, s: str) -> str:
        s = list(s)
        vowels = []
        pos = []
        for i, val in enumerate(s):
            if val in "AEIOUaeiou":
                vowels.append(val)
                pos.append(i)
        vowels.sort()
        for val, index in zip(vowels, pos):
            if val in "AEIOUaeiou":
                s[index] = val
        return "".join(s)
