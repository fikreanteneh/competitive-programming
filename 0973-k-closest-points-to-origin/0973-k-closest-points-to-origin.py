class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        dis = []
        new_dis=[]
        for i in points:
            distance = i[0]**2 + i[1]**2
            dis.append((distance,i))
        dis.sort()
        for j in range(k):
            new_dis.append(dis[j][1])
        return new_dis