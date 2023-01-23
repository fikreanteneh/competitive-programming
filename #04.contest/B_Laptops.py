n = int(input())

temp = []
for i in range(n):
    nums = tuple(map(int, input().split(" ")))
    temp.append(nums)
temp.sort(key = lambda x: x[1])

for i in range(0, n-1):
    if temp[i][0] > temp[i+1][0]:
        print("Happy Alex")
        exit()

print("Poor Alex")