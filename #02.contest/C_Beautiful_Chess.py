n = int(input())


def chess(d1):
    for i in range(1,7):
        for j in range(1,7):
            if d1[i][j] == "#":
                if d1[i-1][j-1] == "#" and d1[i-1][j+1] == "#" and d1[i+1][j-1] == "#" and d1[i+1][j+1] == "#":
                    print(i+1,j+1)
                    return
for i in range(n):
    d1 = []
    for j in range(9):
        f = input()
        if j > 0:
            d1.append(f)
    chess(d1)
