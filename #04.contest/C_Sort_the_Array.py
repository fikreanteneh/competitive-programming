n = int(input())
nums = list(map(int, input().split(" ")))


def answer(n, nums):
    newArr = sorted(nums)
    start = n
    end = 0
    for i, num in enumerate(nums):
        if num != newArr[i]:
            start = min(start, i)
            end = max(end, i)
    if start > end:
        start = end
    if nums[start: end + 1][::-1] == newArr[start:end + 1]:
        print("yes")
        print(start + 1, end + 1) 
    else:
        print("no")
answer(n, nums)
