class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = [[], []]
        players = {}
        for i in matches:
            if i[0] in players: players[i[0]][0]+=1
            else: players[i[0]] = [1, 0]
            if i[1] in players: players[i[1]][1]+=1
            else: players[i[1]] = [0, 1]
        for i, j in players.items():
            if j[1] == 0: winners[0].append(i)
            if j[1] == 1: winners[1].append(i)
        winners[0].sort()
        winners[1].sort()
        return winners
            