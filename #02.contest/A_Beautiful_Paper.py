n = int(input())


def calculate(d1, d2):
    if d1[0] in d2:
        index1 = d2.index(d1[0])
        sums = d1[1] + d2[index1 - 1]
        if sums == d1[0]:
            print("Yes")
            return
    if d1[1] in d2:
        index2 = d2.index(d1[1])
        sums = d1[0] + d2[index2 - 1]
        if sums == d1[1]:
            print("Yes")
            return
    print("No")

for i in range(n):
    d1 = list(map(int, input().split(" ")))
    d2 = list(map(int, input().split(" ")))
    calculate(d1, d2)
