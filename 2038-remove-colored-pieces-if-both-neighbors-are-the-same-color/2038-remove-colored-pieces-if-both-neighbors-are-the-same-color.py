class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        
        turn = colors[0]
        index = 0
        answer = {"A": 0, "B": 0}
        for i, color in enumerate(colors):
            if not (color == turn):
                answer[turn] += max(0, i - index - 2)
                turn = color
                index = i
        answer[turn] += max(0, i - index - 1)
        if answer["A"] > answer["B"]:
            return True 
        return False
    