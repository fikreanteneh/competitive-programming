class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        nums.sort(key = lambda t:int(t))
        return nums[0-k]
