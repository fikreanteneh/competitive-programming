class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        if nums[0] < nums[-1]:
            return nums[0]
        
        left, right = 0, len(nums) - 1
        answer = float("inf")
        while left <= right:
            mid = (left + right)//2
            if nums[left] >= nums[mid] <= nums[right]:
                answer = min(nums[mid], answer)
            if nums[left] <= nums[mid] >= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
        return answer
            