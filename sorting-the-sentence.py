class Solution:
    def sortSentence(self, s: str) -> str:
        word = [None] * 9
        i = 0
        string = ''
        while i < len(s):
            if s[i] != " ": string += s[i]
            if  s[i] == " " or i == len(s)-1: 
                ind = int(string[-1])
                word[ind-1] = string[:-1]
                string = ""
            i+=1
        new = ""
        for i in word:
            if i is None: break
            new = new + i + " "
        return new[:-1]
