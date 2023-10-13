class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        instructions*=(4)
        dx = (0,1)
        pos = { "L": { (0,1): (-1, 0),  (-1, 0):(0,-1),  (0,-1): (1, 0), (1,0): (0,1) }, 
                "R": { (0,1): (1, 0), (1, 0):(0,-1), (0,-1): (-1, 0), (-1,0): (0, 1) }
              }
        curr = [0,0]
        for val in instructions:
            if val == "G":
                curr[0] += dx[0]
                curr[1] += dx[1]
            else:
                dx = pos[val][dx]
        return curr == [0,0]
            
            