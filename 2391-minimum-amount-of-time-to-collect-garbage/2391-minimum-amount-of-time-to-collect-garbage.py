class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        trucks = ["M", "P", "G"]
        travel.append(0)
        ans = 0
        for truck in trucks:
            counted = 0
            for i, grab in enumerate(garbage):
                curr = grab.count(truck)
                if curr:
                    ans += curr
                    ans += counted
                    counted = 0
                counted += travel[i]
                
        return ans
                