class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        store = [[0 for i in range(n + 1)] for j in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                if nums2[i] == nums1[j]:
                    store[i][j] = 1 + store[i + 1][j + 1]
                else:
                    store[i][j] = max(store[i][j + 1], store[i + 1][j])
        return store[0][0]