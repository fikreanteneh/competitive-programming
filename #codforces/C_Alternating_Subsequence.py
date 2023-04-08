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

def solution(n, nums):
    total = 0
    sign = True if nums[0] > 0 else False
    i = 0
    while i < n:
        maxi = float("-inf")
        while i < n and sign == (nums[i] > 0 ):
            maxi = max(nums[i], maxi)
            i += 1 
        total += maxi
        sign = not sign
    return total

t = I()
for _ in range(t):
    n = I()
    nums = LI()
    print(solution(n, nums))
