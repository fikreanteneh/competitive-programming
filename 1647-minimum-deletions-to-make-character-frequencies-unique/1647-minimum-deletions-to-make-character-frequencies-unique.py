class Solution:
    def minDeletions(self, s: str) -> int:
        s = Counter(s)
        s = list(s.items())
        s.sort(key = lambda x: x[1])
        n = len(s)
        prev = s[-1][1]
        answer = 0
        for i in range(n - 2, -1, -1):
            freq = s[i][1]
            if freq >= prev:
                newFreq = prev - 1
                answer += (freq - newFreq)
                freq = newFreq
            prev = freq if freq > 0 else 1
        return answer
            