class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        try:
            index = haystack.index(needle)
            return index
        except:
            return -1
            