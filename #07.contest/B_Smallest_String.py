t = int(input())

def fav(a, b, k):
    a = list(a)
    a.sort()
    b = list(b)
    b.sort()
    ans = []
    i, j = 0, 0
    f, l = 0, 0
    # print(a)
    # print(b)
    # print(k)
    while i < len(a) and j < len(b):
        if a[i] == b[j]:
            ans.append(a[i])
            ans.append(b[j])
            i += 1
            j += 1
        elif (a[i] < b[j] and f < k) or l >= k:
            ans.append(a[i])
            i += 1
            f += 1
            l = 0
        else:
            ans.append(b[j])
            j += 1
            l += 1
            f = 0
    print ("".join(ans))

for te in range(t):
    nums1 = list(map(int, input().split(" ")))
    l1 = input()
    l2 = input()
    # print(nums1)
    # print(l1)
    # print(l2)
    fav(l1,l2, nums1[2])