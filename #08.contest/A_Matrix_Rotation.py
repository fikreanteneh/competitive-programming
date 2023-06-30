t = int(input())

def fav(n1, n2):
    temp = []
    if n1[0] > n1[1]:
        temp.append(1)
    else:
        temp.append(0)

    if n1[1] > n2[1]:
        temp.append(1)
    else:
        temp.append(0)

    if n2[1] > n2[0]:
        temp.append(1)
    else:
        temp.append(0)
    if n2[0] > n1[0]:
        temp.append(1)
    else:
        temp.append(0)

    if tuple(temp) in [(1,1,0,0), (0,1,1,0), (0,0,1,1), (1,0,0,1)]:
        print("YES")
    else:
        print("NO")


for t in range(t):
    nums1 = list(map(int, input().split(" ")))
    nums2 = list(map(int, input().split(" ")))
    fav(nums1, nums2)