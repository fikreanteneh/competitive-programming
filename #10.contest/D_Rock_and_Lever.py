from collections import defaultdict
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


test = I()
for _ in range(test):
    n = I()
    nums = LI()
    x = defaultdict(int)
    ans = 0
    for i in nums:
        y = int(math.log(i, 2))
        ans += x[y]
        x[y] += 1
    print(ans)
