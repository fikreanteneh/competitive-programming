t = int(input())


def maximum(row, col, arr):
    d1 = [0] * (row + col - 1)
    d2 = [0] * (row + col - 1)
    for i in range(row):
        for j in range(col):
            d1[j - i] += arr[i][j]
            d2[i + j] += arr[i][j]
    # print(d1)
    # print(d2)
    # for i in range(row):
    #     for j in range(col):
    #         k = (i+j)
            
    maxi = 0
    for i in range(row):
        for j in range(col):
            maxi = max(maxi, d1[j-i] + d2[i+j] - arr[i][j])
    print(maxi)


for i in range(t):
    grid = list(map(int, input().split(" ")))
    card = []
    for j in range(grid[0]):
        card.append(list(map(int, input().split(" "))))
    maximum(grid[0], grid[1], card)
