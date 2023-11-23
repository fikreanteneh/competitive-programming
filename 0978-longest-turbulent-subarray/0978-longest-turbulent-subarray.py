class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        n = len(arr)
        inc = 1
        dec = 1
        ans = 1
        for i in range(1, n):
            if arr[i - 1] > arr[i]:
                dec = inc + 1
                inc = 1
            elif arr[i - 1] < arr[i]:
                inc = dec + 1
                dec = 1
            else:
                inc = dec = 1
            ans = max( ans, inc, dec )
        return ans
            