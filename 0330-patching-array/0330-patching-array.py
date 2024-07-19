class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        patches = 0
        currSum = 0
        nums.append(float("inf"))
        for i, num in enumerate(nums):
            while currSum < num - 1 and currSum < n:
                patches += 1
                currSum += (currSum + 1)
            currSum += num
            if currSum >= n:
                break
        return patches    