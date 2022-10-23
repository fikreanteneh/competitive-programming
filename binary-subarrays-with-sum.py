class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        ans = 0
        new = [-1]
        for k, num in enumerate(nums):
            if num == 1: new.append(k)
        new.append(len(nums))
        if goal == 0:
            for i in range(1,len(new)):
                n = new[i] - new[i-1] - 1
                ans += (((n + 1)/2) * n)
            return int(ans)
        if new == [0,0]: return 0
        i,j = 1, goal
        for k in range(goal, len(new)-1):
            b = new[i] - new[i-1]
            f = new[j + 1] - new[j]
            ans += (b * f)
            i,j = i+1, j+1
        return ans
    """
    [0,0]
    
    """

                
                
