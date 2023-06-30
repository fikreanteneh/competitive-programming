def LI():
    return list(map(int, input().split(" ")))
def LS():
    return input().split(" ")
def LC():
    return input().split()
def I():
    return int(input())
def S():
    return input()

test = I()

for t in range(test):
    math, program = LI()
    total = math + program
    low = 0
    high = (total) // 4
    maxi = 0
    while low <= high:
        mid = low + (high - low)//2
        if mid <= math and mid <= program and 4 * mid <= total:
            maxi = max(maxi, mid)
            low = mid + 1
        else:
            high = mid - 1
    print(maxi)