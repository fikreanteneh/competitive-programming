class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        for i in range(1, len(arr)):
            arr[i] = arr[i] ^ arr[i -1]
        
        result = [0] * len(queries)
        for j, i in enumerate(queries):
            if i[0] == 0: result[j] = arr[i[1]]
            else: result[j] = arr[i[1]] ^ arr[i[0] - 1]
        return result
