class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        arr.append(inf)
        i, j = 0, 1
        size = 0
        while j < len(arr):
            flag = "increase"
            flag2= False
            i = j - 1
            while (arr[j-1] < arr[j] and flag == "increase") or (arr[j-1] > arr[j] and flag == "decrease"):    
                j += 1
                if j >= len(arr): break
                if arr[j-1] > arr[j]: 
                    flag, flag2 = "decrease", True
            if flag2:
                size = max(size, j-i)
                j -=1
            j = j + 1 
            
        return size
