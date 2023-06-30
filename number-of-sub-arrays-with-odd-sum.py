class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        evenodd= [1, 0]
        ans, sums = 0, 0
        for i in arr:
            sums += i
            if sums%2 == 0: 
                ans += evenodd[1]
                evenodd[0] += 1
            else:
                ans += evenodd[0]
                evenodd[1] += 1
        return ans
                
            
