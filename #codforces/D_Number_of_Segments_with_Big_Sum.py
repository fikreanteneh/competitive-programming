t = list(map(int, input().split(" ")))
n, target = t[0], t[1]
nums = list(map(int, input().split(" ")))
l = sums = 0
segment = 0
for r in range(n):
    sums += nums[r]
    while sums >= target:
        sums -= nums[l]
        l += 1
        segment += (n - r)
print(segment)
