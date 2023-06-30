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


test = I()

for _ in range(test):
    num = I()
    binary = list(bin(num))
    binary.reverse()
    binary.pop()
    binary.pop()
    binary.append("0")
    occ = Counter(binary)
    ans1 = 1 << binary.index("1")
    ans2 = 0
    if occ["1"] <2:
        ans2 = 1<<binary.index("0")
    print(ans1 | ans2)
    
    # occ = {}
    # index = 0
    # while len(occ) < 2:
    #     x = num & 1
    #     if x not in occ:
    #         occ[x] = index
    #     num >>= 1
    #     index += 1
    # check = sorted(occ.values())
    # print(1<<(check[-1]))