class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        answer = []
        block = False
        comment = False
        temp = []
        temp2 = []
        i, j = 0, 0
        while i < len(source):
            line = source[i]
            j = 0
            temp =[]
            while j < len(line):
                word = line[j]
                j += 1
                if block: 
                    if word == "*" and line[j] == "/":
                        temp, temp2 = temp2, []
                        block = False
                        j += 1
                    continue
                elif  word == "/" and j < len(line):
                    if line[j] == "*":
                        temp2, temp = temp, []
                        block = True
                        j += 1
                        continue
                    elif line[j] == "/":
                        break
                temp.append(word)
            if temp: answer.append("".join(temp))
            i += 1
        return answer
            
            
       