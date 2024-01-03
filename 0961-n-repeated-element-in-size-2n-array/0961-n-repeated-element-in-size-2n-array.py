class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        count = Counter(nums)
        n= len(nums) // 2
        for i in nums:
            if count[i] == n:
                return i