# from collections import defaultdict

def fav(n, m, nums1, nums2):
    nums1.sort()
    nums2.sort()
    i = j = 0
    ans = 0
    while i <  n and j < m:
        if abs(nums1[i] - nums2[j]) <= 1:
            ans += 1
            i += 1
            j += 1
        elif nums1[i] < nums2[j] :
            i += 1
        else:
            j += 1
    print(ans)
        

n = int(input())
nums1 = list(map(int, input().split(" ")))
m = int(input())
nums2 = list(map(int, input().split(" ")))
fav(n, m, nums1, nums2)