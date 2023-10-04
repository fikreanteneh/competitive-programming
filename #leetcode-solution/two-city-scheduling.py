class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        temp = sorted([(i-j, (i,j)) for i, j in costs])
        temp.sort()
        ans = 0
        n = len(temp)
        
        for i in range(n//2):
            ans += temp[i][1][0]
            ans += temp[n - 1 - i][1][1] 
        return ans