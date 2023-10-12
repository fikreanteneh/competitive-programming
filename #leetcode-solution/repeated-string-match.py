class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        def checker(a, b):
            try:
                return a.index(b)
            except:
                return -1
        n, m = len(a), len(b)
        repeat = ceil(m/n)
        case1 = checker(a*repeat, b)
        if case1 > -1:
            return repeat
        case1 = checker(a*(repeat + 1) , b)
        if case1 > -1:
            return repeat + 1
        return -1
        