class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        currSum = 0
        for i, num in enumerate(nums):
            if currSum >= n:
                break
            while currSum < num - 1 and currSum < n:
                patches += 1
                currSum += (currSum + 1)
            currSum += num
        while currSum < n:
            patches += 1
            currSum += (currSum + 1)
        return patches    