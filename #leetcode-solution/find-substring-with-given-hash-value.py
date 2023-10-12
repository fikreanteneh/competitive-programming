class Solution:
    def subStrHash(self, s: str, power: int, m: int, k: int, hashValue: int) -> str:
        hashed = 0
        s = s[::-1]
        p = [1]
        for i in range(k - 1):
            p.append( (p[-1]*power)%m)
        for i in range(k - 1):
            lett = ord(s[i]) - 96
            hashed*=power
            hashed += lett
            hashed%=m
        ans = (0,0)
        for i in range(k - 1, len(s)):
            prev, nextt = ord(s[i - k + 1]) - 96, ord(s[i]) - 96
            hashed*=power
            hashed += nextt
            hashed%=m
            if hashed == hashValue:
                ans = (i - k + 1, i + 1)
            hashed -= (prev*p[k-1])
        return s[ans[0]:ans[1]][::-1]
            