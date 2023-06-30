t = int(input())


def answer(nums, n, k):
    ans = 0
    length = k + 1
    nums1 = nums.copy()
    for i in range(1, n):
        nums[i] = nums1[i] / nums1[i-1]
    i, j = 0, 0
    while j < n+1:
        if nums[j] <= 0.5:
            size = j - i
            if size >= length:
                ans += (size - length + 1)
            i = j
        j += 1
    return ans


for i in range(t):
    cond = list(map(int, input().split(" ")))
    n, k = cond[0], cond[1]
    nums = list(map(int, input().split(" ")))
    nums.append(0.1)
    print(answer(nums, n, k))