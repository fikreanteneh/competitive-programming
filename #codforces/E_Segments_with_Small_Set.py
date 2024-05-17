from collections import defaultdict


t = list(map(int, input().split(" ")))
n, target = t[0], t[1]
nums = list(map(int, input().split(" ")))
l = sums = 0
segment = 0
check = set()
for r in range(n):
    while nums[r] in check or len(check) > target :
        check.discard(nums[l])
        l += 1
    check.add(nums[r])
    segment += (r - l + 1)
print(segment)
 