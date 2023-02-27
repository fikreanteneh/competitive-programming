
n = list(map(int, input().split(" ")))
check = n[1]
arr = [0] * 200002


for i in range(n[0]):
    x = list(map(int, input().split(" ")))
    arr[x[0]] += 1
    arr[x[1] + 1] -= 1
    
sums = 0
pre = 0

for i in range(1, 200002):
    sums += arr[i]
    if sums >= check:
        pre += 1
    arr[i] = pre



for i in range(n[2]):
    quest = list(map(int, input().split(" ")))
    print(arr[quest[1]] - arr[quest[0] - 1])