class Solution:
    def printVertically(self, s: str) -> List[str]:
        s = s.split(" ")
        answer = []
        n = 0
        for i in s: n = max(n,len(i))
        for i in range(n):
            temp = []
            for j in s:
                if i >= len(j):
                    temp.append(" ")
                else:
                    temp.append(j[i])
            while temp and temp[-1] == " ": temp.pop()
            answer.append("".join(temp))
        return answer