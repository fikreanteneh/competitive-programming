class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        answer = []
        i = 0
        n = len(nums)
        j = 0
        while i < n:
            if nums[i]:
                j = nums[i]
            while j:
                temp = nums[j-1]
                nums[j-1] = 0
                j = temp
            i += 1

        for i, val in enumerate(nums):
            if val:
                answer.append(i + 1)
        
        return answer