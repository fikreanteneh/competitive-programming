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

# print()
test = I()
for _ in range(test):
    ans = []
    n = I()
    nums = LI()
    check = 0
    for val in nums:
        check ^= val
    # print(check)
    for val in nums:
        if check ^ val == val:
            print(val)
            break
