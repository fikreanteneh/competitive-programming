t = int(input())

def answer(nums):
    nums.sort()
    print(nums[1])


for i in range(t):
    nums = list(map(int, input().split(" ")))
    answer(nums)