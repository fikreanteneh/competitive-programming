from collections import Counter


def fav(toy, row, col, k):
    ans = 0
    if k == 1:
        for i in toy:
            p = Counter(i)
            ans += (p.get(".", 0))
        print(ans)
        return

    for i in range(row):
        empty = 0
        for j in toy[i]:
            if j == ".":
                empty += 1
            else:
                empty = 0
            if empty >= k:
                ans += 1
    for i in range(col):
        seats = [toy[j][i] for j in range(row)]
        empty = 0
        for j in seats:
            if j == ".":
                empty += 1
            else:
                empty = 0
            if empty >= k:
                ans += 1
    print(ans)

    # if k <= col:
    #     for j in range(row):
    #         seats = toy[j]
    #         c = Counter(seats[:k-1])
    #         # print(c, k-1, col-k+1)
    #         for i in range(k-1, col):

    #             c[seats[i]] += 1
    #             # print(c)
    #             if c["."] == k:
    #                 ans += 1
    #             c[seats[i-k]] -= 1

    # # print(ans)
    # if k <= row:
    #     for j in range(col):
    #         seats = [toy[i][j] for i in range(row)]
    #         # print(seats)
    #         c = Counter(seats[:k-1])
    #         for i in range(k-1, row):
    #             c[seats[i]] += 1
    #             # print(c)
    #             if c["."] == k:
    #                 ans += 1
    #             c[seats[i-k]] -= 1
    # print(ans)


nums1 = list(map(int, input().split(" ")))
n, m, k = nums1[0], nums1[1], nums1[2]
toy = []
for i in range(n):
    toy.append(input())
fav(toy, n, m, k)
