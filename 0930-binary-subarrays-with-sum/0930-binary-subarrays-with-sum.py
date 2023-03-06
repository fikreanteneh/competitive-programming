class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        return self.atmost(nums, goal) - self.atmost(nums, goal-1)
    
    def atmost(self, nums, goal):
        count = defaultdict(int)
        ans = left = sums = 0
        for right in range(len(nums)):
            sums += nums[right]
            while left <= right and sums > goal:
                sums -= nums[left]
                left += 1
            ans += (right - left + 1)
        return ans
                
        
        
 