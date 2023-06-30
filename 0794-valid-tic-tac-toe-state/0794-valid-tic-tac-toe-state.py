class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        player = {"X": 0, "O": 0, " ":0}
        for i in board:
            for j in i:
                player[j] += 1
        if player["O"] > player["X"]: return False
        elif player["O"] + 2 <= player["X"]: return False
        
        for i in board:
            if i == "XXX":
                if player["X"] <= player["O"]:
                    return False
            elif i == "OOO":
                if player["X"] != player["O"]:
                    return False
                
        for i in range(3):
            cur = "".join([board[0][i], board[1][i], board[2][i]])
            if "XXX" == cur:
                if player["X"] <= player["O"]:
                    return False
            elif "OOO" == cur:
                if player["X"] != player["O"]:
                    return False
        
        for i in range(2):
            cur = "".join([board[0][0 - (i*1)], board[1][1 - (i*3)], board[2][2 - (i*5)]])
            if "XXX" == cur:
                if player["X"] <= player["O"]:
                    return False
            elif "OOO" == cur:
                if player["X"] != player["O"]:
                    return False
                
        return True