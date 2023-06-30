n = int(input())
arr = list(map(int, input().split()))
pairs = []


for i in range(len(arr)):
    index = i
    for j in range(i + 1, len(arr)):
        
        if arr[index] > arr[j]:
            index = j
            
            
    if index != i:
        pairs.append((i, index))
        arr[index], arr[i] = arr[i], arr[index]

print(len(pairs))
for res in pairs:
    print(*res)