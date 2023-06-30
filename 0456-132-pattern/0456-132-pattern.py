class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        nums.reverse()
        n = len(nums)
        check = float("-inf")
        for i,num in enumerate(nums):
            if num < check:
                return True
            while stack and stack[-1] < num:
                check = stack.pop()
            stack.append(num)
        return False
    # 4 3 0 5 3
    # 3 5 0 3 4 