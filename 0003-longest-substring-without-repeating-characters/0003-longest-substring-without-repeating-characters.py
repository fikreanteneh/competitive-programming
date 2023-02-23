class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maximum = 0
        new = [[],[]]
        i, j = 0,0
        for i in range(len(s)):
            if s[i] in new[0]:
                x = new[0].index(s[i])
                j = x + 1
                new[0], new[1] = new[0][x+1:], new[1][x+1:]
            new[0].append(s[i])
            new[1].append(i)
            maximum = max(maximum, new[1][-1] - new[1][0] + 1)
        return maximum