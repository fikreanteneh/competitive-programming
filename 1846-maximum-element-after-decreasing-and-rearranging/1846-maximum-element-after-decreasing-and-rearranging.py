class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()
        arr[0] = 1
        for i in range(1, len(arr)):
            x, y = arr[i-1], arr[i]
            if y - x <= 0:
                continue
            else:
                arr[i] = x + 1
        
        return arr[-1]
            
            
            