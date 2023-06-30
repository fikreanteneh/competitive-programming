n = int(input())
nums = list(map(int, input().split(" ")))

def answer(n, nums):
    nums.sort()
    if nums[-1] >= nums[-2] + nums[-3]:
        print("NO")
        return
    nums[-1], nums[-2] = nums[-2], nums[-1]
    print("YES")
    print(*nums)
    

answer(n,nums)