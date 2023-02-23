t = int(input())


def fav(n, words):
    ans = []
    check = set(words)
    # for i, word in enumerate(words):
    #     words[i] = (word, i)
    # words.sort()


    for i in words:
        appended = "0"
        for j in range(len(words)):
            if i[:j] in check and i[j:] in check:
                appended = "1"
                break
        ans.append(appended)

    print("".join(ans))


for t in range(t):
    words = []
    n = int(input())
    for i in range(n):
        words.append(input())
    fav(n, words)
