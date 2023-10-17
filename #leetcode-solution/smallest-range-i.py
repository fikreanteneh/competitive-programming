class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        y, x = max(nums), min(nums)
        k <<= 1
        return max( 0, (y - x) - k )
