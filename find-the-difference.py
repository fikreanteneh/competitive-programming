class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sets = {}
        for i in t: sets[i] = sets.get(i, 0) + 1
        for i in s: 
            sets[i] -= 1
            if sets[i] == 0: sets.pop(i)
        return tuple(sets)[0]
