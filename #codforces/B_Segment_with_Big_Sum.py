t = list(map(int, input().split(" ")))
n, target = t[0], t[1]
nums = list(map(int, input().split(" ")))
l = sums = 0
mini = float("inf")
for r in range(n):
    sums += nums[r]
    while sums >= target:
        sums -= nums[l]
        mini = min(mini, r - l + 1)
        l += 1
if mini == float("inf"):
    print(-1)
else:
    print(mini)
