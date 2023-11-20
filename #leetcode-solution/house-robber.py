class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 2:
            return max(nums)
        follow = [-1, -1]
        sums = [nums[0], nums[1]]
        take = [True, True]
        if nums[0] > nums[1]:
            follow[-1] = 0
            sums[-1] = nums[0]
            take[-1] = False
        
        for i in range(2, n):
            if sums[i - 1] >= sums[i - 2] + nums[i]:
                follow.append(i - 1)
                sums.append( sums[i - 1] )
                take.append(False)
            else:
                follow.append(i - 2)
                sums.append( sums[i - 2] + nums[i] )
                take.append(True)
                
            
        answer = []
        n -= 1
        while n > -1:
            if take[n]:
                answer.append(n)
            n = follow[n]
        ans = 0
        for i in answer:
            ans += nums[i]
        return ans
            
                