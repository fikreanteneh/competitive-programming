class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix = [1]
        suffix  = [1]
        p = s = 1
        for i in range(n):
            p *= nums[i]
            prefix.append(p)
            s *= nums[n - 1 - i]
            suffix.append(s)
        suffix.reverse()
        
        for i in range(n):
            nums[i] = prefix[i] * suffix[i+1]
        return nums
        
