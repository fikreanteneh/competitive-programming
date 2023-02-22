class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        sums = sum(nums[:k])
        maxi = sums / k
        
        for i in range(k, len(nums)):
            sums -= nums[i-k]
            sums += nums[i]
            maxi = max(maxi, sums/k)
            
        return maxi