class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        store = [False]*128
        left, right =0, 1
        n = len(s)
        ans = 0
        for right in range(n):
            while left < right and store[ ord(s[right])]:
                store[ ord(s[left])] = not store[ ord(s[left])]
                left += 1
            
            store[ ord(s[right])] = True
            ans = max(ans,  right -left + 1)
        return ans
                