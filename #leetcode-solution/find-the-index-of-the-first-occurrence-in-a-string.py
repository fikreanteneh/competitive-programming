class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n, m = len(haystack), len(needle)
        if m > n:
            return -1
        alpha = 27
        MULTIPLY = [alpha**i for i in range(m)]
        MOD = 10**9 + 7
        haystackHash = 0
        needleHash = 0
        for i in range(m - 1):
            val = ord(haystack[i]) - 96
            haystackHash += (val*MULTIPLY[m - i - 2])
            val = ord(needle[i]) - 96
            needleHash += (val*MULTIPLY[m - i - 1])
        needleHash += ( ord(needle[m-1]) - 96)
        
        for i in range(m - 1, n):
            haystackHash*=alpha
            haystackHash += (ord(haystack[i]) - 96)
            if haystackHash == needleHash:
                return i - m + 1
            haystackHash -= ( (ord(haystack[i - m + 1]) - 96)*MULTIPLY[m - 1])
        return -1

            
         
        ########################################
        j = 0
        for i, val in enumerate(haystack):
            if val == needle[j]:
                j += 1
            else:
                j = 0
            if j >= len(needle) :
                return i - (j - 1)
        return -1
            
        #######################################
        try:
            index = haystack.index(needle)
            return index
        except:
            return -1
            