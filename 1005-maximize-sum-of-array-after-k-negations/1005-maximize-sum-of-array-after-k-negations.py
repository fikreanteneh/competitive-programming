class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums.append(float("inf"))
        i = 0
        while nums[i] < 0 and nums[i + 1] < 0 and k > 0:
            nums[i] = -nums[i]
            k -= 1
            i += 1
        if k:
            nums[i] = -nums[i]
            k -= 1

        if nums[i] < nums[i + 1]:
            index = i
        else:
            index = i + 1
            
        if k % 2:
            nums[index] = -nums[index] 
        nums.pop()
        return sum(nums)