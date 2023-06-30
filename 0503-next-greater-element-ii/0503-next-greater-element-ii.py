class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack, ans = [], [-1]*n
        for i, num in enumerate(nums):
            while stack and stack[-1][0] < num: 
                ans[stack.pop()[1]] = num
            stack.append((num,i))
        for i, num in enumerate(nums):
            while stack and stack[-1][0] < num: 
                ans[stack.pop()[1]] = num
        return ans