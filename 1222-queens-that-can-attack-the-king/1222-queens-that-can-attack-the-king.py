class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set(tuple(i) for i in queens)
        x, y = king[0], king[1]
        answer = []
        DIR = [(1, 1), (1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]
        for row, col in DIR:
            self.recursive(row, col, answer, x, y, queens)
        return answer
    
    def is_bound(self, row, col):
        return 0 <= row < 8 and 0 <= col < 8
        
    def recursive(self, row, col, answer, new_x, new_y, queens):
        while self.is_bound(new_x, new_y):
            new_x += row
            new_y += col
            if (new_x, new_y) in queens:
                answer.append([new_x, new_y])
                break
    
        