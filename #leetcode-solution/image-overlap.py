class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        store = set()
        check = []
        n = len(img1)
        for i in range(n):
            for j in range(n):
                if img1[i][j]:
                    store.add((i, j))
                if img2[i][j]:
                    check.append((i, j))
        answer = 0
        for i in range(0, 2*n + 1):
            for j in range(0, 2*n + 1):
                # rows, cols = 2*n - i, 2*n - j
                # print("---", i, j)
                ans = 0
                for x, y in check:
                    # print(n - x - i , n - y - j)
                    # print(x, y)
                    if (n + x - i , n + y - j) in store:
                        ans += 1
                # print(ans)
                answer = max(answer, ans)
        return answer
                
        