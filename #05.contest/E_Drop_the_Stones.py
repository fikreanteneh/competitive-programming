n = int(input())


def shortest(row, col, arr):
    for i in range(col):
        end = row
        # print("for col", i)
        for j in range(row, -1, -1):
            # print(arr[j][i], j, i)
            if arr[j][i] == "*":
                arr[j][i], arr[end][i] = arr[end][i], arr[j][i]
                # print("ff")
                end -= 1
            elif arr[j][i] == "o":
                end = j - 1
            # for k in range(row + 1):
            #     print(*arr[k])
            # print("llllllllll for", j, end)
    for i in range(row + 1):
        print("".join(arr[i]))


for i in range(n):
    req = list(map(int, input().split(" ")))
    given = []
    for j in range(req[0]):
        given.append(list(input()))
    shortest(req[0] - 1, req[1], given)
