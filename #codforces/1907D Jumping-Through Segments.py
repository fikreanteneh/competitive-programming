t = int(input())

for _ in range(t):
    n = int(input())
    seg = []
    for i in range(n):
        a, b = list(map(int, input().split()))
        seg.append((a, b))
    
    def good_function(mid):
        a, b = -mid, mid
        for x, y in seg:
            value = [(a, b), (x, y)]
            value.sort()
            if value[0][1] < value[1][0]:
                return False
            a = max(a, x) - mid
            b = min(b, y) + mid
        return True
    l, r = 0, 10 ** 9
    # print(good_function(0))
    while l < r:
        mid = (l + r) // 2
        if good_function(mid):
            r = mid
        else:
            l = mid + 1
    print(l)