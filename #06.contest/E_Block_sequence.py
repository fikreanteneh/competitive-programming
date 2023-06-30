

def fav(wid, hei, nums):
    if wid == 1:
        print(0)
        return
    nums.sort()

    ans  = nums[0] - 1
    # if ans < 0:
    #     ans = 0
    ans = 0
    prev = 0
    for i in range(1,len(nums)):
        block = nums[i]
        x = nums[i - 1]
        ans += x
        if x != block:
            
            prev = i

        if x == block:
            ans -= (x - 1)
    print(ans)
 
n = list(map(int, input().split(" ")))
nums = list(map(int, input().split(" ")))
fav(n[0],n[1], nums)

10 17
12 16 6 9 12 6 12 1 12 13

1  6  6  9  12  12  12  12  13  16
0  1  6  6  9   12  12  12  12  13

3  3   3  3 3
0  2  2   2 2
