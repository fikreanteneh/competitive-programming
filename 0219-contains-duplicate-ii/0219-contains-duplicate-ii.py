class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        store = {} # 1:3, 2:1, 3:2, 1
        for i, num in enumerate(nums):
            # index = store.get(num, float("-inf"))
            if num in store:
                index = store[num]
                if i - index <= k:
                    return True
            store[num] = i
        
        
        return False