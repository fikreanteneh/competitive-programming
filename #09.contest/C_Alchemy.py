length = int(input())
times = list(map(int, input().split()))

x = 0
y = length - 1
xt = 0
yt = 0
e_ct = 0
al_ct = 0

while x <= y:
    if xt <= yt:
        xt += times[x]
        x += 1
        e_ct += 1
    else:
        yt += times[y]
        y -= 1
        al_ct += 1

print(e_ct, al_ct)