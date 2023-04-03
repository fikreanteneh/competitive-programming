# from math import ceil


# def LI():
#     return list(map(int, input().split(" ")))


# def LS():
#     return input().split(" ")


# def LC():
#     return input().split()


# def I():
#     return int(input())


# def S():
#     return input()


# n, enemy = LI()
# player = LI()

# player.sort()
# i, j = 0, n-1
# ans = 0
# while j > i:
#     req = enemy / player[j]
#     if req < 0:
#         ans += 1
#         j -=1
#         continue
#     req = int(req)
#     new = req
#     while req > 0 and i <= j:
#         i += 1
#         req -= 1
#     if player[j] * (new + 1) <= enemy:
#         break
#     if not req:
#         ans += 1
#     if i == j:
#         break
#     # print("--", i, j)
#     j -= 1
# print(ans)

from math import ceil
 
 
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
 
 
n, enemy = LI()
player = LI()
 
player.sort()
i, j = 0, n-1
ans = 0
while j >= i:
    if player[j] > enemy:
        ans += 1
        j -= 1
        continue
    x  = enemy / player[j]
    i += int(x)
    if i > j:
        break
    ans += 1
    j -= 1

print(ans)