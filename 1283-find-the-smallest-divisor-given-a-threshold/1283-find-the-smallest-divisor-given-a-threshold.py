class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 1, max(nums)
        mini = float("inf")
        while left <= right:
            mid = left + (right - left) // 2
            sums = 0
            for i in nums:
                sums += (ceil(i / mid))
            
            if sums > threshold:
                left = mid + 1
            else:
                mini = min(mini, mid)
                right = mid - 1
        
        return mini