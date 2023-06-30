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

a, b = LI()


def euclid(x, y):
    if  y == 0:
        return x
    return euclid(y, x%y)

x = euclid(a, b)
for i in range(a+1, b):
    x = euclid(i, x)
    if x == 1:
        break

print(x)