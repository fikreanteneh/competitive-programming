class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        count = [0]*101
        total = 0
        for i in arr: count[i] += 1
        for i in range (101):
            for j in range(i, 101, 1):
                k = target - i - j
                if not (0 <= k <= 100): continue
                elif i == j == k:
                    total += (count[i] * (count[i]-1) * (count[i] - 2) / 6)
                elif i == j != k:
                    total += (count[k] * (count[i] * (count[i]-1) / 2))
                elif i < j < k:
                    total += (count[i] * count [j] * count [k])
        return int (total % (10**9 + 7))
