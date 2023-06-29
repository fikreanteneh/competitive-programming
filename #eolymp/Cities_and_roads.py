def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()

n = I()

graph = []
for _ in range(n):
    graph.append(LI())


answer = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        answer += graph[i][j]

print(answer)