class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s = dict(Counter(s))
        t = list(Counter(t).items())
        for i in t:
            value = s.get(i[0], 0)
            if i[1] != value: return i[0]