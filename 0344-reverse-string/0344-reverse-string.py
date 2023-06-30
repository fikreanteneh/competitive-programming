class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        self.solution(s, 0, len(s)-1)
    
    def solution(self, s, l, r):
        if l >= r:
            return
        s[l], s[r] = s[r], s[l]
        self.solution(s, l + 1, r - 1)