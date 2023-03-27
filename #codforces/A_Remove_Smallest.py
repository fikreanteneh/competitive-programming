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
for test in range(t):
    n = I()
    nums = LI()
    flag = False
    nums.sort()
    for i in range(1, n):
        if nums[i] - nums[i - 1] > 1:
            flag = True
            break
    
    if flag:
        print("NO")
    else:
        print("YES")