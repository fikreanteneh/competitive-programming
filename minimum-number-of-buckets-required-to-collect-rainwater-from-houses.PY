class Solution:
    def minimumBuckets(self, street: str) -> int:
        sum, n = 0, len(street)
        road = []
        for i, space in enumerate(street):
            if space == ".": continue
            x = y = None
            if i != 0 and street[i-1] == "." : x = i - 1
            if i != n-1 and street[i+1] == ".": y = i + 1
            if x == y: return -1
            elif not road: road.append((x,y))
            elif x == road[-1][1]!=None: 
                sum +=1
                road.pop()
            else:
                sum +=1
                road[-1] = (x,y)   
                
        if len(road) == 1: sum+=1
        return sum
        """for i in range(len(road)):
            if road[i] == (None, None): continue
            elif i != 0 and road[i][0] == road[i-1][1] != None: road[i-1] = (None, None)
            elif i != len(road) - 1 and road[i][1] == road[i+1][0] != None: road[i+1] = (None, None)
            road [i] = (None, None)
            sum += 1"""
        
            
            
