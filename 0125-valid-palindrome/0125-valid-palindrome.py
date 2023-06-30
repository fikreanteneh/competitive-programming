class Solution:
    def isPalindrome(self, s: str) -> bool:
        # letters = []
        # for i in s:
        #     if i.isalpha(): letters.append
        i, j = 0, len(s) - 1
        l, r = 0, 0
        while i < j:
            if not s[i].isalnum(): i+= 1
            elif not s[j].isalnum(): j-= 1
            else:
                if s[i].lower() != s[j].lower(): return False
                i, j = i+1, j-1
        return True