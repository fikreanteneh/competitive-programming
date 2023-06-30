class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        new = []
        new.append(intervals[0])
        for i in range(1, len(intervals)):
            point1 = new[-1]
            point2 = intervals[i]

            if point2[0] > point1[1]:
                new.append(point2)
            else:
                if point1[1] < point2[1]: point1[1] = point2[1]
        return new
