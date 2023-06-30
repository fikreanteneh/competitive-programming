class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        n, m = len(houses), len(heaters)
        i, j = 0, 0
        store1 = [float("inf")] * n
        while i < n and j < m - 1:
            x = abs(houses[i] - heaters[j])
            y = abs(houses[i] - heaters[j + 1])
            if x < y:
                store1[i] = x
                i += 1
            else:
                j += 1

        for i, num in enumerate(store1):
            store1[i] = min(abs(heaters[-1] - houses[i]), num)
        return max(store1)