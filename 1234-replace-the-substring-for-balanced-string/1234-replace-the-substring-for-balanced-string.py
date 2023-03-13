class Solution:
    def balancedString(self, s: str) -> int:
        n = len(s)
        required = n//4
        count = Counter(s)
        extra = defaultdict(int)
        answer = float("inf")
        for i,j in count.items():
            if j > required:
                extra[i] = j - required
        
        if len(extra) == 0:
            return 0
        
        left = 0
        for right, val in enumerate(s):
            if val in extra:
                extra[val] -= 1
            while left <= right and max(extra.values()) <= 0:
                answer = min(answer, right - left + 1)
                if s[left] in extra:
                    extra[s[left]] += 1
                left += 1
        return answer
        
        