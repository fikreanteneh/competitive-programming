from collections import Counter


t = int(input())
for i in range(t):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    ans = 0
    i = 0
    while i < n-1 and nums[i] == 0:
        i += 1
    for j in range(i, n-1):
        if nums[j] == 0:
            ans += 1
    ans += (sum(nums[:n-1]))
    print(ans)