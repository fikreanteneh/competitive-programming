t = list(map(int, input().split(" ")))
n, target = t[0], t[1]
nums = list(map(int, input().split(" ")))
l = sums = 0
segment = ans = 0
for r in range(n):
    sums += nums[r]
    while sums > target:
        sums -= nums[l]
        l += 1
    segment += r - l + 1
print(segment)
