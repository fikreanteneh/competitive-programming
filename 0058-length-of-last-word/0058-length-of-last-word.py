class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(" ")
        while s and s[-1] == "":
            s.pop()
        return len(s[-1])
        