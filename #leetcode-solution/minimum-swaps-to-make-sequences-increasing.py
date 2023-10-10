class Solution:
    def minSwap(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        store = [ [float("inf"),float("inf"),0],[float("inf"),float("inf"),0]]
        for index in range(n - 1, -1, -1):
            first = [nums1[index], nums2[index], float("inf")]
            second = [nums2[index], nums1[index], float("inf")]
            if nums1[index] <store[0][0] and nums2[index] < store[0][1]:
                first[2] = min(first[2], store[0][2])
            if nums1[index] <store[1][0] and nums2[index] < store[1][1]:
                first[2] = min(first[2], store[1][2])
            if nums2[index] <store[0][0] and nums1[index] < store[0][1]:
                second[2] = min(second[2], store[0][2] + 1)
            if nums2[index] <store[1][0] and nums1[index] < store[1][1]:
                second[2] = min(second[2], store[1][2] + 1)
            store = [first, second]
        return min(store[0][2], store[1][2])
        
                
                
#                 first = sol(index + 1, nums1[index], nums2[index], curr)
#             second = float("inf")
#             if a < nums2[index] and b < nums1[index]:
#                 second = sol(index + 1, nums2[index], nums1[index], curr + 1)
#             return min(first, second)
            
            
#         @cache
#         def sol(index, a, b, curr):
#             if index >= n:
#                 return curr
#             first = float("inf")
#             if a < nums1[index] and b < nums2[index]:
#                 first = sol(index + 1, nums1[index], nums2[index], curr)
#             second = float("inf")
#             if a < nums2[index] and b < nums1[index]:
#                 second = sol(index + 1, nums2[index], nums1[index], curr + 1)
#             return min(first, second)
#         return sol(0, -1, -1, 0)