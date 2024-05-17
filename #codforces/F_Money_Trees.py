# Author: Fikremariam Anteneh  Asegie
# Link: https://codeforces.com/problemset/problem/1873/F



def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return list(input())
def I(): return int(input())
def S(): return input()


def longestSubarrayWithSumLessThanK(fruits, leftP, rightP, k):
    total = 0
    size = 0
    left = 0
    for right in range(leftP, rightP):
        total += fruits[right]
        while total > k:
            total -= fruits[left]
            left += 1
        size = max(size, right - left + 1)
    print(leftP, rightP, "------->",size)
    return size


def sol():
    n, k = LI()
    fruits = LI()
    arr = LI()
    slices = []
    left = 0
    for right in range(1, n):
        if arr[right]%arr[right - 1] != 0:
            slices.append((left, right))
            left = right
    slices.append((left, n))
    ans = 0
    for left, right in slices:
        ans = max(ans, longestSubarrayWithSumLessThanK(fruits, left, right, k))
    print(ans)






    

            




t= I()
for _ in range(t):
    sol()