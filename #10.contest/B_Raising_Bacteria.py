import math


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


num = I()

ans = 0
while num >= 2:
    x = int(math.log(num, 2))
    # print(x, "--")
    ans += 1
    num = num - (2**(x))
ans += num
print(ans)