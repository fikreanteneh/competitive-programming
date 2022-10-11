class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        pos = [(0,0)]* 1002
        maxi = 0
        for i in trips: 
            pos[i[1]] = (pos[i[1]][0] + i[0] , pos[i[1]][1])
            pos[i[2]] = (pos[i[2]][0] , pos[i[2]][1]  + i[0])
            maxi = max(maxi, i[2])
        sum, pos = 0, pos[:maxi + 2]
        for i in pos:
            sum = sum + i[0] - i[1]
            if sum > capacity: return False
        return True
