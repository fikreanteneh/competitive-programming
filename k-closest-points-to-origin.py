class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
         values = []
         for i in points:
             z = (i[0]**2) + (i[1]**2)
             values.append((z, i))
         values.sort()
         values = values[:k]
         new = []
         for i in values:
             new.append(i[1])
         return new
