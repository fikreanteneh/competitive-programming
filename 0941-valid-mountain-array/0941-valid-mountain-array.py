class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        n = len(arr)
        if n < 3: return False
        check = 1
        i = 1
        while i < n and arr[i-1] < arr[i]:
            i += 1
        if check == i or i == n: return False
        while i < n and arr[i-1] > arr[i]:
            i += 1
        return i == n