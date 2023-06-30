class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        answer =  (-1, float("inf"))
        for i, point in enumerate(points):
            if x == point[0] or y == point[1]:
                distance = abs(x - point[0]) + abs(y - point[1])
                if  distance < answer[1]: answer = (i, distance)
        return answer[0]
                