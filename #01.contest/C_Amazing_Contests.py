n = int(input())
lists = list(map(int, input().split(" ")))

def pronounce(n, lists):
    if n == 1:
        print(0)
        return
    maxi = mini = lists[0]
    answer = 0
    for i in lists:
        if i < mini or i > maxi:
            answer += 1
        mini = min(mini, i)
        maxi = max(maxi, i)
    print(answer)


pronounce(n, lists)
