class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        
        nums = list(map(str, nums))
        n = len(nums)
        for i in range(1, n):
            index = i
            for j in range(i - 1, -1, -1):
                right, left = nums[index], nums[j]
                if int(left + right) > int(right + left):
                    break
                nums[index], nums[j] = nums[j], nums[index]
                index -= 1
        
        return str(int("".join(nums)))