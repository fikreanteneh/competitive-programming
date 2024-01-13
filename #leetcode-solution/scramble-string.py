class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        
        @cache
        def dp(s1, s2):
            if sorted(s1) != sorted(s2):
                return False
            if s1 == s2:
                return True
            n = len(s1)
            for i in range(1, len(s1)):
                if dp(s1[:i], s2[:i]) and dp(s1[i:], s2[i:]):
                    return True
                if dp(s1[:i], s2[n-i:]) and dp(s1[i:], s2[:n-i]):
                    return True
            return False
        return dp(s1, s2)