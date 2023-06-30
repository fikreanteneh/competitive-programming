class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        index = {n:i for i, n in enumerate(nums1)}
        final = [-1] * len(nums1)
        stack = []
        for i in nums2:
            while stack and stack[-1] < i:
                final[index[stack.pop()]] = i
            if i in index: stack.append(i)
        return final
