class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        ans = []
        nums.sort()
        for i, num in enumerate(nums):
            if num == target:
                ans.append(i)
        return ans