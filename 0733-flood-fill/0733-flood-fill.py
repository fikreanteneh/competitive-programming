class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        m = len(image)
        n = len(image[0])
        visited = set()
        def solution(row, col):
            if (row,col) in visited:
                return
            neighbors = [(row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)]
            cur = image[row][col]
            image[row][col] = color
            visited.add((row,col))
            for i, j in neighbors:
                if -1 < i < m and -1 < j < n and image[i][j] == cur:
                    solution(i, j)
                
        solution(sr, sc)
        return image