# https://codeforces.com/problemset/problem/1971/F


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return list(input())
def I(): return int(input())
def S(): return input()



def numOfLatticePointExclusive(radius):
    answer = radius*4  + 1 # The Cross in x+ x- y+ y- direction and 0
    quarterCircle = 0
    x = radius
    check = radius**2
    for y in range(1, radius):
        y2 = y**2
        newRadius = x**2 + y2
        while newRadius >= check:
            x -= 1
            newRadius = x**2 + y2
        quarterCircle += x
    answer += quarterCircle*4
    return answer


# if __name__ == "main":
t = I()
for _ in range(t):
    n = I()
    print(numOfLatticePointExclusive(n + 1) - numOfLatticePointExclusive(n))