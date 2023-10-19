class Solution:
    def unhappyFriends(self, n: int, preferences: List[List[int]], pairs: List[List[int]]) -> int:
        preferences = [ {val: i for i, val in enumerate(row)} for row in  preferences]
        pairRank = [None]*n
        for x, y in pairs:
            pairRank[x] = preferences[x][y]
            pairRank[y] = preferences[y][x]
        ans = set()
        for i, preference in enumerate(preferences):
            for j in range(i + 1, n):
                if preferences[j][i] < pairRank[j] and preferences[i][j] < pairRank[i]:
                    ans.add(i)
                    ans.add(j)
        return len(ans)
                