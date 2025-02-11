class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int, version1.split(".")))
        v2 = list(map(int, version2.split(".")))

        padding = [0]*abs(len(v1) - len(v2))
        v2.extend(padding) if len(v1) > len(v2) else v1.extend(padding)

        if v1 == v2: 
            return 0
        elif v1 < v2:
            return -1
        return 1