class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = {num for num in range(len(nums)+1)}
        for i in nums:
            numbers.discard(i)
        numbers = list(numbers)
        return numbers[0]
        