n = int(input())
nums = list(map(int, input().split(" ")))


def programing(nums, n):
    nums.sort()
    i = 0
    maxi = 1
    for j in range(1, n):
        while nums[j] - nums[i] > 5:
            i += 1
        maxi = max(maxi, j - i + 1)


    print(maxi)


programing(nums, n)
