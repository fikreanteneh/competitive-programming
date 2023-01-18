from collections import defaultdict
from collections import Counter

n = int(input())


def pronounce(word):
    answer = []
    for i in range(2):
        answer.append(word[i])
    answer.append("... ")
    answer.append(word)
    answer.append("?")
    print("".join(answer))


for k in range(n):
    word = input()
    pronounce(word)
