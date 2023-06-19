class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        memo = defaultdict(int)
        
        for i, val in enumerate(arr):
            prev = memo[val - difference]
            memo[val] = prev + 1
            
        
        return max(memo.values())
            
        