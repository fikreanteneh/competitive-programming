class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        curr = 0
        for i, val in enumerate(pref):
            pref[i] = curr^val
            curr = val
        return pref