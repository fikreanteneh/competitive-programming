


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


n, m = LI()

x, y = list(bin(n)), list(bin(m))
x.reverse()
y.reverse()
for i in range(2):
    x.pop()
    y.pop()
for i in range(len(y) - len(x)):
    x.append("0")

x.reverse()
y.reverse()
n = len(y)
i = 0
while i < n and y[i] == x[i]:
    i += 1 

for i in range(i + 1, n):
    y[i] = "1"
    x[i] = "0"

x = int("".join(x), 2)
y = int("".join(y), 2)
print(x ^ y)
        
