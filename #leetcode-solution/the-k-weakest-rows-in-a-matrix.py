class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        ans = []
        for i, row in enumerate(mat):
            ans.append((row.count(1), i))
        ans.sort()
        return [ans[i][1] for i in range(k)]
            