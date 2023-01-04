class Solution:
    def queensAttacktheKing(self, queens: List[List[int]], king: List[int]) -> List[List[int]]:
        queens = set(tuple(i) for i in queens)
        x, y = king[0], king[1]
        answer = []
        def is_bound(row, col):
            return 0 <= row < 8 and 0 <= col < 8
        def recursive(row, col):
            nonlocal x
            nonlocal y
            new_x  = x
            new_y = y
            while is_bound(new_x, new_y):
                new_x += row
                new_y += col
                if (new_x, new_y) in queens:
                    answer.append([new_x, new_y])
                    break
        DIR = [(1, 1), (1, 0), (0, 1), (-1, -1), (-1, 0), (0, -1), (-1, 1), (1, -1)]
        for row, col in DIR:
            recursive(row, col)
        return answer
    
        