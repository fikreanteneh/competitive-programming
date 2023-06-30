t = int(input())

def fav(n, nums):
    ans = []
    i, j = 0, n - 1
    flag = True
    while i <= j:
        if flag:
            ans.append(nums[i])
            i += 1
            flag = False
        else:
            ans.append(nums[j])
            j -= 1
            flag = True 
    print(*ans)

for i in range(t):
    n = int(input())
    nums = list(map(int, input().split(" ")))
    fav(n, nums)