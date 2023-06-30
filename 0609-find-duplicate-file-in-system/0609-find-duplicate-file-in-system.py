class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        contentsPath = defaultdict(list)
        for i in paths:
            files = i.split(" ")
            path = files[0]
            for j in range(1, len(files)):
                file = files[j]        
                indexLast = len(file)
                index = indexLast - 1
                while index and file[index] != "(":
                    index -= 1
                content = file[index + 1: indexLast]
                contentsPath[content].append(path + "/" + file[:index])
        answer = []
        for i,j in contentsPath.items():
            if len(j) > 1:
                answer.append(j)
        return answer
            
            
        