t = int(input())

def calculate(arr, n, m = 0, sums = 0):
    if n-m <= 0:
        return sums
    for i in range(0, n - m):
        indexes = ((m, m + i), (m + i ,n), (n, n - i), (n-i, m))
        count = {0:0, 1:0}
        for x,y in indexes:
            count[arr[x][y]] += 1
        sums += min(count[0], count[1])
    return calculate(arr, n - 1, m + 1, sums)


for i in range(t):
    n = int(input())
    arr=[]
    for i in range(n):
        arr.append(list(map(int, list(input()))))
    print(calculate(arr, n-1))