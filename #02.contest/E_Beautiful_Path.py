
def crosing (arr,i,j,n,m, char):
    for row in range(i-1,-1,-1):
        if arr[row][j] == ".":
            arr[row][j] = char
        else:
            break
    for row in range(i+1,n):
        if arr[row][j] == ".":
            arr[row][j] = char
        else:
            break
    for col in range(j-1,-1,-1):
        if arr[i][col] == ".":
            arr[i][col] = char
        else:
            break
    for col in range(j+1,m):
        if arr[i][col] == ".":
            arr[i][col] = char
        else:
            break
def check(arr, n, m):
    
    for i in range(n):
        last = "*"
        for j in range(m):
            if (arr[i][j], last) == ("T", "S") or (arr[i][j], last) == ("S", "T"):
                return True
            if arr[i][j] != ".":
                last = arr[i][j]
    for j in range(m):
        last = "*"
        for i in range(n):
            if (arr[i][j], last) == ("T", "S") or (arr[i][j], last) == ("S", "T"):
                return True
            if arr[i][j] != ".":
                last = arr[i][j]
    return False
t = list(map(int, input().split(" ")))
n, m = t[0], t[1]
arr = []
for i in range(n):
    arr.append(list(input()))
indexes = {}
for i in range(n):
    for j in range(m):
        val = arr[i][j]
        if val in "ST":
            indexes[val] = (i, j)

s, t = indexes["S"], indexes["T"]
crosing(arr,s[0],s[1],n,m,"S")
crosing(arr,t[0],t[1],n,m,"T")


if check(arr, n, m):
    print("YES")
else:
    print("NO")
