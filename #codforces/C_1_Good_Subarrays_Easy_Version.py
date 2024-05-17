# Author: Fikremariam Anteneh  Asegie
# Link: https://codeforces.com/problemset/problem/1736/C1
# Time complexity: O(nlogn, 1)  and O(n, 1)

from bisect import bisect_right


def LI(): return list(map(int, input().split(" ")))
def LS(): return input().split(" ")
def LC(): return list(input())
def I(): return int(input())
def S(): return input()

def sol():
    n = I()
    arr = LI()
    ans = 0

    # Binary Search
    for left in range(n):
        right = bisect_right(arr, left+1)
        



    # Slidding Window
    right = 0
    curr =  1
    for left in range(n):
        while right < n and arr[right] >= curr:
            curr += 1
            right += 1
        length =  right - left
        ans += length
        curr -= 1
    print(ans)

            




t= I()
for _ in range(t):
    sol()