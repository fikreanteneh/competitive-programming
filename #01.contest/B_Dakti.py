n = int(input())


def pronounce(word):
    answer = []
    for i in word:
        temp = []
        index = []
        for j in i:
            if j.isnumeric():
                index.append(j)
            else:
                temp.append(j)
        temp = "".join(temp)
        index = "".join(index)
        answer.append((index, temp))
    answer.sort()
    for i, ans in enumerate(answer):
        answer[i] = ans[1]
    print(" ".join(answer))


for k in range(n):
    word = input().split(" ")
    pronounce(word)
