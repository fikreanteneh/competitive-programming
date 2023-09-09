class Solution:
    def appealSum(self, s: str) -> int:
        lastPos = [-1] * 26
        answer, curr = 0, 0
        
        for i, letter in enumerate(s):
            index = ord(letter) - ord("a")
            curr = curr + (i - lastPos[index])
            answer += curr
            lastPos[index] = i
            
        return answer
            