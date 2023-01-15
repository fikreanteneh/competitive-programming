class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        if n < 3 or m < 0: return ans
        def calculate(arr):
            if sorted(arr) == [1,2,3,4,5,6,7,8,9]:
                r1 = arr[0] + arr[1] + arr[2]
                r2 = arr[3] + arr[4] + arr[5]
                r3 = arr[6] + arr[7] + arr[8]
                c1 = arr[0] + arr[3] + arr[6]
                c2 = arr[1] + arr[4] + arr[7]
                c3 = arr[2] + arr[5] + arr[8]
                d1 = arr[0] + arr[4] + arr[8]
                d2 = arr[2] + arr[4] + arr[6]
                return r1==r2==r3==c1==c2==c3==d1==d2
            return False
                
        for i in range(0,n-2):
            for j in range(0, m-2):
                if calculate( [ grid[i][j],   grid[i][j+1],   grid[i][j+2],
                          grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                          grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2] ]):
                    ans += 1
        return ans
            