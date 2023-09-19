class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        #cyclyc sort
        # while nums[0] != nums[nums[0]]:
        #     index, value = nums[0], nums[nums[0]]
        #     nums[nums[0]], nums[0] = index, value
        # return nums[0]
        
        
        # With Floyd
        tortoise, rabbit = 0,0
        while True:
            tortoise = nums[tortoise]
            rabbit = nums[nums[rabbit]]
            if tortoise == rabbit:
                break
        
        tortoise2 = 0
        while True:
            tortoise = nums[tortoise]
            tortoise2 = nums[tortoise2]
            if tortoise == tortoise2:
                return tortoise
            
                
                