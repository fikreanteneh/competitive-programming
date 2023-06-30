from math import ceil


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


t = I()

for _ in range(t):
    n, h = LI()
    attacks = LI()

    if n >= h:
        print(1)
        continue
    if n == 1:
        print(h)
        continue

    low, high = 0, h
    curr = float("inf")
    attacks.append(float("inf"))

    while low <= high:
        mid = low + (high - low) // 2
        damage = 0
        for i in range(n):
            att = attacks[i + 1] - attacks[i]
            damage += (min(att, mid))
        if damage == h:
            curr = mid
            break
        if damage < h:
            low = mid + 1
        else:
            curr = min(curr, mid)
            high = mid - 1
    print(curr)
