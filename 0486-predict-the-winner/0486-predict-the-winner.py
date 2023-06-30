class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        ans = self.solution(nums, 0, 0, len(nums) - 1)
        print("last", ans)
        return ans[0] >= ans [1]  
    
    def solution(self, nums, turn, left, right):
        if right - left == 0:
            ans = [0, 0]
            ans[turn] += nums[left]
            return ans
        
        elif right - left == 1:
            ans = [0, 0]
            ans[turn] += max(nums[left], nums[right])
            ans[1 - turn] += min(nums[left], nums[right])
            return ans
        
        first = self.solution(nums, 1 - turn, left + 1, right)
        first[turn] += nums[left]
        
        second = self.solution(nums, 1 - turn, left, right-1)
        second[turn] += nums[right]
        
        
        return first if first[turn] >= second[turn] else second