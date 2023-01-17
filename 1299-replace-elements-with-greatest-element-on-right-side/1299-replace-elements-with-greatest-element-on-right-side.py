class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        great = -1
        for i in range(len(arr) - 1, -1, -1):
            great, arr[i] = max(great, arr[i]), great
        return arr
        