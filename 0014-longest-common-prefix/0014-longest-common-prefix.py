class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[-1]
        # if not prefix: return ""
        p = 0
        while p < len(prefix):
            for i in strs:
                if p == len(i) or prefix[p]!= i[p]: return prefix[:p]
            p += 1
        return prefix[:p]
            