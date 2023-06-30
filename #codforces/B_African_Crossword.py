def LI():
    return list(map(int, input().split(" ")))
def LS():
    return input().split(" ")
def LC():
    return input().split()
def I():
    return int(input())
def S():
    return input()


row, col = LI()
answer = []

for i in range(row):
    answer.append(list(input()))

toBeRemoved = []
for i in range(row * col):
    x = i % col
    y = i // col
    char = answer[y][x]
    # print(i)
    # print(y, x, "row, col")
    # print("   ")
    flag = False
    for onRow in range(x + 1, col):
        # print(y, onRow, "onrow", answer[y][onRow] == char)

        if answer[y][onRow] == char:
            toBeRemoved.append((y,onRow))
            flag = True
    # print("   ")
    for onCol in range(y + 1, row):
        # print(y, onCol, "oncol", answer[onCol][x] == char)
        if answer[onCol][x] == char:
            toBeRemoved.append((onCol, x))
            flag = True
    if flag:
        toBeRemoved.append((y, x))
    # print(toBeRemoved)
    # print("   ")

# print(toBeRemoved)
for i in toBeRemoved:
    answer[i[0]][i[1]] = ""
# print(answer)
for i, val in enumerate(answer):
    answer[i] = "".join(val)

print("".join(answer))


