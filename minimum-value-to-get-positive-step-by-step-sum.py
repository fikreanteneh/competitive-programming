class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        number,sum = 1, 0
        nums[0] += 1
        for i in (nums): 
            sum += i 
            if sum <= 0: 
                number += (abs(sum) + 1)
                sum += (abs(sum) + 1)
        return number
