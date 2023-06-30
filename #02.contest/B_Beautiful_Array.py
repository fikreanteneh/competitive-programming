n  = int(input())
d1 = list(map(int, input().split(" ")))

zero, neg, pos = [], [], []
n, z,p = 0 ,0,0
for i in d1:
    if i < 0:
        n += 1
        neg.append(i)
    elif i == 0:
        z+= 1
        zero.append(i)
    else:
        p += 1
        pos.append(i)

if p == 0:
    pos.append(neg.pop())
    pos.append(neg.pop())
    n -= 2
    p+=2
if n%2 == 0:
    zero.append(neg.pop())
    z += 1
neg = list(map(str, neg))
zero = list(map(str, zero))
pos = list(map(str, pos))
print(str(len(neg))," ".join(neg))
print(str(len(pos))," ".join(pos))
print(str(len(zero))," ".join(zero))
