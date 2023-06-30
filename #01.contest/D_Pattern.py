
n = int(input())
lists = []
for i in range(n):
    lists.append(input())


def pronounce(lists):
    answer = []
    for i in range(len(lists[0])):
        letter = "?"
        flag = False
        for j in lists:
            if letter == "?" and j[i] != "?":
                letter = j[i]
            elif letter != "?" and j[i] != "?" and letter != j[i]:
                letter = "?"
                flag = True
                break
        if flag:
            answer.append("?")
        elif letter == "?":
            answer.append("x")
        else:
            answer.append(letter)

    print("".join(answer))


pronounce(lists)
