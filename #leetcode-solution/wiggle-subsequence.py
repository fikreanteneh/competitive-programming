class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1 or n == 2 and nums[0] != nums[1]:
            return n
        i = 1
        while i < n and nums[i] == nums[i - 1]:
            i += 1
        if i == n:
            return 1
        stack = [nums[i - 1], nums[i]]
        target = "small" if nums[i - 1] < nums[i] else "big"
        for j in range(i + 1, n):
            if target == "big":
                if nums[j] > nums[j - 1]:
                    stack.append(nums[j])
                    target = "small"
                else: 
                    stack[-1] = nums[j]
            if target == "small":
                if nums[j] < nums[j - 1]:
                    stack.append(nums[j])
                    target = "big"
                else:
                    stack[-1] = nums[j]
        return len(stack)
                
                