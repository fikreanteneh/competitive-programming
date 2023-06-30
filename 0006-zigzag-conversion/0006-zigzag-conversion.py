class Solution:
    def convert(self, s: str, numRows: int) -> str:
        answer = []
        if numRows == 1: return s
        for i in range(0, len(s), numRows*2 - 2):
            answer.append(s[i])
        for j in range(1, numRows - 1):
            for i in range(j, len(s), numRows*2 - 2 ):
                answer.append(s[i])
                x = i + numRows*2 - 2 - (2 * j)
                if x < len(s):
                    answer.append(s[x])
        for i in range(numRows - 1, len(s), numRows*2 - 2):
            answer.append(s[i])
        return "".join(answer)
    
        """
        p               i
          a         l
            y    a
              p
        
        
        """
        