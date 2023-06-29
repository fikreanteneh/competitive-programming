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
source = {i for i in range(1, n+1)}
sink = {i for i in range(1, n+1)}
for i in range(n):
    row = LI()
    for j in range(n):
        if row[j]:
            source.discard(j+1)
            sink.discard(i+1)

print(len(source), *source)
print(len(sink), *sink)
