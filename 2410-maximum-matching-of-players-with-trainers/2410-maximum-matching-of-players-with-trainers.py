class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()
        i, j = 0, 0
        n, m = len(players), len(trainers)
        ans = 0
        while i < n and j < m:
            if players[i] <= trainers[j]:
                ans += 1
                i += 1
            j += 1
        return ans
            