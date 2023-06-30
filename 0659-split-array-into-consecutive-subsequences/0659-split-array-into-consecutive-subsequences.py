class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        
        store = defaultdict(list)
        for val in nums:
            prev = 0 if val - 1  not in store or len(store[val - 1]) == 0 else heappop(store[val - 1])
            heappush(store[val], prev + 1)
    
        for i, j in store.items():
            if j and j[0] < 3:
                return False
        
        return True
        
        