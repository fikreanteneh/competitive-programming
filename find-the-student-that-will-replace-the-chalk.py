class Solution:
    def chalkReplacer(self, chalk: List[int], k: int) -> int:
        sums = 0
        for i in chalk: sums += i
        k = k - (k//sums * sums)
        for j, i in enumerate(chalk):
            if i > k: return j
            k -= i
