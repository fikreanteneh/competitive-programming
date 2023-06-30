from heapq import heapify, heappop, heappush
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


num, k = LI()

x = bin(num)
answer = []
curr = 1
for i in range(len(x)-1, 1, -1):
    if x[i] == "1":
        answer.append(-1 * curr)
    curr <<= 1

heapify(answer)
while len(answer) < k and answer[0] < -1:
    x = heappop(answer)
    y = x // 2
    heappush(answer, y)
    heappush(answer, y)

if len(answer) != k:
    print("NO")
else:
    for i, val in enumerate(answer):
        answer[i] = -1 * val
    print("YES")
    answer.reverse()
    print(*answer)

