class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        ans = float("inf")
        prefix = deque([(0, -1)])
        runningSum = 0
        
        for right, num in enumerate(nums):
            runningSum += num
            
            while prefix and runningSum - prefix[0][0] >= k:
                ans = min(ans, right - prefix[0][1])
                prefix.popleft()
                
            while prefix and runningSum <= prefix[-1][0]:
                prefix.pop()
                
            prefix.append([runningSum, right])
        
        return -1 if ans == float("inf") else ans 
    

