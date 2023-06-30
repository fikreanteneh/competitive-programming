

def fav(n, nums):
    temp = [0,0,0]
    ans = 0
    for i in nums:
        if i < 0:
            temp[-1] += 1
            ans += (-1 - (i))
        elif i > 0:
            temp[1] += 1
            ans += (i - 1)
        else:
            temp[0] += 1
    if temp[0] == 0 and temp[-1] % 2 == 1:
        ans += 2
    else:
        ans += (temp[0])
    print(ans)



n = int(input())
nums = list(map(int, input().split(" ")))
fav(n, nums)