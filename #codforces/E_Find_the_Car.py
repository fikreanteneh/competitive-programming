# https://codeforces.com/problemset/problem/1971/E
from bisect import bisect_right
from itertools import accumulate


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return list(input())
def I(): return int(input())
def S(): return input()

def calculate(points, times, queries):
    answer = []
    for point in queries:
        index = bisect_right(points, point)
        ans = times[index - 1]
        distance = points[index] - points[index - 1]
        time = times[index] - times[index - 1]
        speed = distance/time
        ans += ( (point - points[index - 1])/ speed)
        answer.append(int(ans))
    return answer


t = I()
for _ in range(t):
    n, k, q = LI()
    points = [0] + LI()
    times = [0] + LI()
    points.append(points[-1] + 1)
    times.append(points[-1] + 1)
    queries = []
    for _ in range(q):
        queries.append(I())
    print(*calculate(points, times, queries))