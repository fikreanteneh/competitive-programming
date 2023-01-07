class Solution:
    def grayCode(self, n: int) -> List[int]:
        results = [0]
        for i in range(n):
            x = len(results)
            for j in range(x-1, -1,-1):
                results.append( 2**i + results[j])
        return results
    # i = 0:      [0, 1]
    # i = 1:      [0, 1, 3, 2]
    # i = 2:      [0, 1, 3, 2, 6, 7, 5, 4]
    