def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return input().split()
def I(): return int(input())
def S(): return input()



n = I()
answer = 0
for i in range(n):
    row = LI()
    for j in range(i):
        answer += row[j]

print(answer)