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

n, m , k = LI()
emo = LI()
emo.sort()
i = m // (k+1)

ans =  i * (emo[-1] *k + emo[-2]) + (m % (k+1) * emo[-1]) 
print(ans)