class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        n = len(spaces)
        if n == 0: return s
        answer = []
        j = spaces[0]
        answer = [s[0:j]]
        answer.append(" ")
        for i in range(1, len(spaces)):
            index = spaces[i]
            answer.append(s[j:index])
            answer.append(" ")
            j = index
        index = spaces[-1]
        answer.append(s[index:])
        return "".join(answer)
        
            