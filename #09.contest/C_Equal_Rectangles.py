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



t  = I()
for test in range(t):
    n = I()
    stick = LI()

    count = 0
    flag = False

    stick.sort()
    area = stick[-1] * stick[0]

    m = len(stick)

    for i in range(0, len(stick)//2, 2):
        a = stick[i] * stick[m - 1 - i]

        if a != area or stick[i] != stick[i + 1] or stick[m-1-i] != stick[m-2-i]:
            print("NO")
            flag = True
            break
        count += 1
    if flag:
        continue
    elif count == n:
        print("YES")
    else:
        print("NO")
