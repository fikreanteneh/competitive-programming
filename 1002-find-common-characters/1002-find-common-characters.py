class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        letters = [0] * 26
        letters = self.count(words[0])
        for i in words:
            temp = self.count(i)
            for k, tem in enumerate(temp):
                letters[k] =  min(letters[k],tem)
        ans = []
        for i, rep in enumerate(letters):
            if rep > 0:
                for j in range(rep):
                    ans.append(chr(i + 97))
        return ans
    def count(self, lists):
        temp = [0] * 26
        for i in lists:
            temp[ord(i) - 97] += 1
        return temp