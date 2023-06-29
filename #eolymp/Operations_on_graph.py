from collections import defaultdict


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


n = I()
o = I()

graph = defaultdict(list)

for i in range(o):
    op = LI()
    if op[0] == 1:
        graph[op[1]].append(op[2])
        graph[op[2]].append(op[1])
    else:
        print(*graph[op[1]])
