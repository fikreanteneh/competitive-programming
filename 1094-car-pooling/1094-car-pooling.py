class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        path = [0] * 1001
        for i in trips:
            path[i[1]] += i[0]
            path[i[2]] -= i[0]
        
        sums = 0
        for i, pa in enumerate(path):
            sums += pa
            # print(i, "---", sums)
            if sums > capacity:
                return False
        return True
        