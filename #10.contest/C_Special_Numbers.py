

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

modulo = 10**9 + 7

test = I()
for _ in range(test):
    n, k = LI()
    k = list(bin(k))
    k.reverse()
    k.pop()
    k.pop()
    ans = 0
    for i, val in enumerate(k):
        if val == "1":
            ans += (n ** i)
    print(ans%modulo)
    
