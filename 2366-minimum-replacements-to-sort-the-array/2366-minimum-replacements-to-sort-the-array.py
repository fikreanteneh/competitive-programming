class Solution:
    def minimumReplacement(self, nums: List[int]) -> int:
        nums.reverse()
        mini = nums[0]
        ops = 0
        for i in range(1, len(nums)):
            num = nums[i]
            ops += ceil(num/mini) - 1
            mini = floor(num/(ceil(num/mini)))
        return ops
            
      
            
        