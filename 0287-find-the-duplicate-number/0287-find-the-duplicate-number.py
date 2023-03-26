class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        answer = []
        index = 0
        n = len(nums)
        while index < n:
            cycle = index 
            
            while nums[index] and nums[index] - 1 != index:
                idx = nums[index] - 1
                temp = nums[idx]
                if temp - 1 == idx:
                    return temp
                    break
                nums[index],  nums[idx] = nums[idx], nums[index]
            index += 1

                