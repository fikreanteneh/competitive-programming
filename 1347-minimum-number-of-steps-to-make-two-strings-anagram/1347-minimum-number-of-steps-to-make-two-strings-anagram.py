class Solution:
    def minSteps(self, s: str, t: str) -> int:
        sCount = Counter(s)
        ans = 0
        for i in t:
            sCount[i] = max(0, sCount[i] - 1 )
        return sum(sCount.values())