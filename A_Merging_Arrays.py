n = list(map(int, input().split(" ")))
num1 = list(map(int, input().split(" ")))
num2 = list(map(int, input().split(" ")))

array = []
i, j = 0, 0
while i < len(num1) and j < len(num2):
    if num1[i] < num2[j]:
        array.append(num1[i])
        i += 1
    elif num1[i] > num2[j]:
        array.append(num2[j])
        j += 1
    else:
        array.append(num1[i])
        i += 1
        array.append(num2[j])
        j += 1
while i < len(num1):
    array.append(num1[i])
    i += 1
while j < len(num2):
    array.append(num2[j])
    j += 1
print(*array)
