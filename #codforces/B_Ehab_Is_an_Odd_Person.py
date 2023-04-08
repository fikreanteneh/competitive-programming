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


# https://codeforces.com/problemset/problem/1174/B

n = I()
nums = LI()
flag = False
for i in range(1, n):
    if (nums[i] + nums[i-1]) % 2 == 1:
        flag = True
        break
if flag:
    nums.sort()
print(*nums)