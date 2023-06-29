from collections import defaultdict


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()


def coloring(graph, n):
    # print(graph)
    colorType = [-1] * (n + 1)
    que = [(1,0)]
    while que:
        node, color = que.pop()
        if colorType[node] not in (-1, color):
            return False
        if colorType[node] == color:
            continue
        colorType[node] = color
        for child in graph[node]:
            que.append((child, 1 - color))
    # print(colorType)
    return True

while True:
    try:
        n = I()
        e = I()
        graph = [[] for _ in range(n + 1)]
        for i in range(e):
            edge = LI()
            graph[edge[0]].append(edge[1])
            graph[edge[1]].append(edge[0])
        canBeColored = coloring(graph, n)
        # print(canBeColored)
        print("BICOLOURABLE." if canBeColored else "NOT BICOLOURABLE.")
    except:
        break