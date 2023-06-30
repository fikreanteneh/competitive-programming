n = int(input())
nums = list(map(int, input().split(" ")))


def nondecrease(nums, n):
    i = 1
    maxi = 1
    ans = 0
    while i < n:
        if nums[i] >= nums[i-1]:
            ans += 1
            maxi = max(ans + 1, maxi)
        else:
            ans = 0
        i += 1

    print(maxi)


nondecrease(nums, n)
