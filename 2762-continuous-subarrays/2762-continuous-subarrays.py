class Solution:
    def continuousSubarrays(self, nums: List[int]) -> int:
        # Hash Map
        store = defaultdict(int)
        left = 0
        count = 0
        for right, num in enumerate(nums):
            store[num] += 1
            while max(store.keys()) - min(store.keys()) > 2:
                store[nums[left]] -= 1
                if store[nums[left]] == 0:
                    del store[nums[left]]
                left += 1
            count += right - left + 1
        return count
                
        
        # Monotonic Queue
        maxi, mini = deque([]), deque([])
        count = 0
        left = 0
        for right, num in enumerate(nums):
            while maxi and maxi[0][0] < num:
                maxi.popleft()
            while mini and mini[0][0] > num:
                mini.popleft()
            maxi.appendleft((num, right))
            mini.appendleft((num, right))
            while maxi[-1][0] - mini[-1][0] > 2:
                if nums[left] == maxi[-1][0]:
                    maxi.pop()
                if nums[left] == mini[-1][0]:
                    mini.pop()
                left += 1
            count += right - left + 1
        return count
                