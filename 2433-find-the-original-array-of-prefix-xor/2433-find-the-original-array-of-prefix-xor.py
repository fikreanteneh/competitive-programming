class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        
        def calc(pref1, pref2):
            num = ""
            for i in range(21, -1, -1):
                p1 = (pref1 >> i) & 1
                p2 = (pref2 >> i) & 1
                num += str( p1^p2  )
            return int(num, 2)
        curr = 0
        for i, val in enumerate(pref):
            pref[i] = calc(curr, val)
            curr = val
        return pref