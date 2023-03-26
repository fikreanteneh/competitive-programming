class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        answer = []
        index = 0
        n = len(nums)
        while index < n:
            cycle = index 
            
            while nums[index] and nums[index] - 1 != index:
                idx = nums[index] - 1
                temp = nums[idx]
                if temp - 1 == idx:
                    answer.append(temp)
                    nums[index] = 0
                    break
                nums[index],  nums[idx] = nums[idx], nums[index]
            index += 1
        
        for i, num in enumerate(nums):
            if num-1 != i:
                answer.append(i + 1)
                break
        return answer