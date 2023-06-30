class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        new = []
        for i in range(min(len(word1), len(word2))):
            new.append(word1[i])
            new.append(word2[i])
        for j in range(i + 1, len(word1)): new.append(word1[j])
        for j in range(i + 1, len(word2)): new.append(word2[j])
        return "".join(new)
        
        