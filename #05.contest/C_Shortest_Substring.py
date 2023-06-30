n = int(input())

def check(n):
    if n[1] > 0 and n[2]>0 and n[3] > 0:
        return True
    return False

def shortest(word):
    mini = float("inf")
    rep = [0,0,0,0]
    i, j = 0, 0
    while j < len(word):
        rep[int(word[j])] += 1
        while check(rep):
            mini = min(mini, j - i + 1)
            rep[int(word[i])] -= 1
            i += 1
        j += 1
    return mini if mini != float("inf") else 0

for i in range(n):
    print(shortest(input()))