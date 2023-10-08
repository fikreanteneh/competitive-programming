class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        x, y = max(nums1), min(nums1)
        a, b = max(nums2), min(nums2)
        if x < 0 and b > 0:
            return x*b
        if y > 0 and a < 0:
            return y*a
        
        store = [ [0 for i in range(m+1)] for i in range(n+1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                store[i][j] = max( nums1[i]*nums2[j] + store[i + 1][j + 1], store[i][j + 1], store[i + 1][j] )
        return store[0][0]