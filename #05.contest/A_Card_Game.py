n= int(input())
arr = list(map(int, input().split()))
def maxScore(n, arr):
    points = [0, 0]
    left , right = 0 , n - 1
    index = 0
    while left <= right:
        if arr[left] > arr[right]: 
            points[index] += arr[left]
            left += 1
        else:
            points[index] += arr[right]
            right -= 1
        index = 1 - index
    return points
print(*maxScore(n, arr))