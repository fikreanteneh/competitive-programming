class Solution:
    def reverseWords(self, s: str) -> str:
        newWord = [ word[::-1]  for word in s.split(" ") ]
        return " ".join(newWord)