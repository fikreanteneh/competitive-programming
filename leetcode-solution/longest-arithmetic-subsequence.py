class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        n = len(nums)
        store = [defaultdict(lambda: 1) for _ in range(n)]
        answer = float("-inf")
        for i in range(1, n):
            for j in range(i - 1, -1, -1):
                if nums[i] - nums[j] not in store[i]:
                    store[i][nums[i] - nums[j]] += store[j][nums[i] - nums[j]]
                    answer = max(answer, store[i][nums[i] - nums[j]])        
        return answer
                
                