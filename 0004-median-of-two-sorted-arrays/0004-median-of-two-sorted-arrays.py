class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        arr1, arr2 = (nums1, nums2) if len(nums1) <= len(nums2) else (nums2, nums1)
        n, m = len(arr1), len(arr2)
        length = n + m
        middle = (length + 1) // 2
        arr1.extend([float("inf"), float("-inf")])
        arr2.extend([float("inf"), float("-inf")])
        left, right = 0, n 
        while left <= right:
            i = (left + right) // 2
            j = middle - i
            if arr1[i - 1] <= arr2[j] and  arr2[j - 1] <= arr1[i]:
                break
            elif arr1[i - 1] > arr2[j]:
                right = i - 1
            else:
                left = i + 1
        if length % 2: 
            return max(arr1[i - 1], arr2[j - 1])
        x, y = max(arr1[i - 1], arr2[j - 1]), min(arr1[i], arr2[j])
        return (x + y) / 2
        