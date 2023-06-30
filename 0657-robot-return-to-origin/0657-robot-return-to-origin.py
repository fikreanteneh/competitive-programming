class Solution:
    def judgeCircle(self, moves: str) -> bool:
        mapp = {"U": [0,1], "D": [0, -1], "R": [1, 0], "L": [-1, 0]}
        pos = [0, 0]
        for i in moves:
            x, y = mapp[i]
            pos[0] += x
            pos[1] += y
        
        
        return pos == [0, 0]