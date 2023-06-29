from collections import defaultdict


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()

n = I()
connection = {i: [] for i in range(n)}

def adjacencyMatrix(i, matrix):
    for j in range(n):
        if matrix[j]:
            connection[i].append(j+1)
    return connection


for i in range(n):
    adjacencyMatrix(i, LI())

for i in range(n):
    print( len(connection[i]),*connection[i])