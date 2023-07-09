class Solution:
    def checkRecord(self, s: str) -> bool:
        chance = {"A":0, "L": 0}
        
        for i in s:
            if i == "A":
                chance["A"] += 1
                if chance["A"] >= 2:
                    return False
                chance["L"] = 0
            elif i== "L":
                chance["L"] += 1
                if chance["L"] >= 3:
                    return False
            else:
                chance["L"] = 0
        return True