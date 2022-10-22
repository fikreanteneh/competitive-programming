class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        prefix = [[0]*26]
        ans = []
        for i in range(len(s)):
            count = [0] * 26
            count[ord(s[i])-97] += 1
            for k in range(26): count[k] += prefix[-1][k]
            prefix.append(count)
        for l, r, c in queries:
            check = self.ccc(prefix[l], prefix[r + 1])
            odd = 0
            if (r-l) % 2 == 0: c += 1
            for j in check:
                if j % 2 != 0: odd += 1
            if c >= odd: ans.append(True)
            elif odd - c <= c : ans.append(True)
            else: ans.append(False)
        return ans
    def ccc(self, l, r):
        new = [0] * 26
        for i in range(26):
            new[i] = r[i] - l[i]       
        return new
