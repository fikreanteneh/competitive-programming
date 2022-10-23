class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        changed.sort()
        nums = dict(Counter(changed))
        answer = []
        if 0 in nums and nums[0] % 2 != 0: return []
        elif nums.get(0,0) > 0: 
            answer  = [0]*(nums.get(0,0)//2)
            nums.pop(0)
        while len(nums) > 0:
            key = next(iter(nums))
            while nums[key] != 0:
                if key * 2 not in nums: return []
                answer.append(key)
                nums[key] -= 1
                nums[key * 2] -= 1
            nums.pop(key)
            if nums[key * 2] == 0: nums.pop(key * 2)

        return answer
                
