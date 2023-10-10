class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters.append(float("inf"))
        ans = 0
        for i, val in enumerate(houses):
            index = bisect_left(heaters, val)
            ans = max(ans, min(abs(heaters[index]-val), abs(heaters[index - 1]-val)))
        return ans
         
        