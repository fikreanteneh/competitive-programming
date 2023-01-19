class Solution:
    def lastRemaining(self, n: int, m = 1, index = 1) -> int:
        return self.calculate([1, n], 0, 1)
        
    def calculate(self, track, index, level):
        differ = track[1] - track[0]
        if differ <= 0:
            return track[1 - index]
        track[index] += ( ((0-index) * 2 * level) + level )
        if (differ / level) % 2 == 0:
            track[1-index] += ( (0-(1-index)) * 2 * level + level )
        return self.calculate(track, 1 - index, level * 2)