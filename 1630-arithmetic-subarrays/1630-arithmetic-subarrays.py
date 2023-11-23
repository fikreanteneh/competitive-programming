class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        n = len(l)
        ranges = []
        ans = [True] * n
        for i in range(n):
            x = nums[ l[i] : r[i] + 1]
            x.sort()
            ranges.append(x)
        for i in range(n):
            num = ranges[i]
            for j in range(2, len(num)):
                if num[j] - num[j - 1] != num[j - 1] - num[j - 2]:
                    ans[i] = False
                    break
        return ans
                    