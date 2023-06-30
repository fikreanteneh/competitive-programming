class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        for idx, word in enumerate(words):
            temp = 0
            for i in word:
                temp |= 1 << (ord(i) - 97)
            words[idx]= (temp, len(word))
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words[i][0] & words[j][0] == 0:
                    ans = max(ans, words[i][1] * words[j][1])
        return ans