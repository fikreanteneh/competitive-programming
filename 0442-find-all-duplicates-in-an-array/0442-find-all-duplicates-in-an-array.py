class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
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
                # print(nums, answer, index)
            index += 1
                
        # print(nums)
        return answer
                