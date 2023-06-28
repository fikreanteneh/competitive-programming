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

def adjacencyMatrix(matrix):
    graph = defaultdict()
    n = len(matrix)
    for i in range(n):
        graph[i+1] = set()
        for j in range(n):
            if matrix[i][j]:
                graph[i+1].add(j+1)
    return graph

def edgeList(edge):
    graph = defaultdict(lambda: set())
    for i, j in edge:
        graph[i].add(j)
