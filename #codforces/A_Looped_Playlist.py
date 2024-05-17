t = list(map(int, input().split(" ")))
n, target = t[0], t[1]
nums = list(map(int, input().split(" ")))

sums = sum(nums)

c = target//sums

target = target % sums
ans = l = 0

mini = [float("inf"), float("-inf")]

for r in range(2 * n + 1):
    ans += nums[r % n]
    while ans >= target:
        if mini[0] - mini[1]  > r - l: 
            mini = [r, l]
        ans -= nums[l % n]
        l += 1

print(mini[1] % n + 1 , c*n + mini[0] - mini[1] + 1)
