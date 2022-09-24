#User function Template for python3

class Solution: 
    def select(self, arr, i):
        # code here
        min = i
        num = arr[i]
        for j in range(i, len(arr)):
            if arr[j] < num:
                min, num =j, arr[j]
        return min
    
    def selectionSort(self, arr,n):
        #code here
        for j in range(n):
            index = self.select(arr, j)
            arr[j], arr[index] = arr[index],arr[j]
