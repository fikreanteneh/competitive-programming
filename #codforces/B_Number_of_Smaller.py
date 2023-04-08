n = list(map(int, input().split(" ")))
x, y = n[0], n[1]
arr1 = list(map(int, input().split(" ")))
arr2 = list(map(int, input().split(" ")))
 
i = 0
ans = []
for num in (arr2):
    while i < x and arr1[i] < num:
        i += 1
    ans.append(i)
print(*ans)