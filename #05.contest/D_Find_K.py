n = int(input())

def check(n):
    if n[1] > 0 and n[2]>0 and n[3] > 0:
        return True
    return False

def shortest(m, k, arr):
    check = set(arr)
    for i in arr:
        if i-k in check:
            return "YES"
    return "NO"

for i in range(n):
    req = list(map(int, input().split(" ")))
    given = list(map(int, input().split(" ")))
    print(shortest(req[0], req[1], given))