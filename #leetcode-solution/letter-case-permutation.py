class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        ans = [""]
        n = len(s)
        
        for i in range(n):
            nextt = []
            for val in ans:
                if s[i].isalpha():
                    nextt.append(val + s[i].upper())
                    nextt.append(val + s[i].lower())
                else:
                    nextt.append(val + s[i])
            ans = nextt
                    

        return ans