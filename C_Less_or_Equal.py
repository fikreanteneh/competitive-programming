t = list(map(int, input().split(" ")))
n, target = t[0], t[1]

nums = list(map(int, input().split(" ")))
nums.sort()
# print(nums)
check = nums[target-1] + 1
# print("--", check)
if target > n:
    print(-1)
elif check < nums[ (target) % n]:
    print(check)
else:
    print(-1)
