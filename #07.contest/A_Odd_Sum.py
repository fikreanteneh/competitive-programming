# from collections import defaultdict

def fav(n, nums):
    nums.sort()
    if sum(nums[:n]) != sum(nums[n:]):
        print(*nums)
        return
    print(-1)
        

n = int(input())
nums = list(map(int, input().split(" ")))
fav(n, nums)