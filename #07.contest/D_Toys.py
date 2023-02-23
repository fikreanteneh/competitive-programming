from collections import Counter

def calculate(price, toy, n, m):
    ans = [0,0]
    price.sort()
    toy = Counter(toy)
    toy = list(toy.items())
    toy.sort(key = lambda x : x[1])
    x, y = 0, len(toy) - 1
    while x < n and y >= 0:
        ans[0] += (price[x] * toy[y][1])
        x += 1
        y -= 1
    x, y = n-1, len(toy) - 1
    while x >= 0 and y >= 0:
        ans[1] += (price[x] * toy[y][1])
        x -= 1
        y -= 1
    print(*ans)

nums1 = list(map(int, input().split(" ")))
n, m = nums1[0], nums1[1]
price = list(map(int, input().split(" ")))
toy = []
for n in range(m):
    toy.append(input())
calculate(price, toy, n, m)