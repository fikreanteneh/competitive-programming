from collections import Counter


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

prime = set()
prime.add(2)
almost = 0
rang = I()

for num in range(3, rang + 1):
    temp = []
    for p in prime:
        if num % p == 0:
            temp.append(p)
    divisors = len(Counter(temp))
    if not divisors:
        prime.add(num)
    elif divisors == 2:
        almost += 1
print(almost)

n = 10000
num = [i for i in range(n+1)]
for i in num:
    for j in range(i, int(num **(0.5)), i):
        x = i * j
        if x > n:
            break
        num[i * j] = 0
print(set(num))