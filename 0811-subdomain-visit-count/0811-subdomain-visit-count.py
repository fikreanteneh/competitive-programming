class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visitCount = defaultdict(lambda : 0 )
        for i in cpdomains:
            numIndex = 0
            n = len(i)
            while numIndex < n and i[numIndex].isnumeric():
                numIndex += 1
            repeat = int(i[0:numIndex])
            for index in range(n-1, numIndex - 1 , -1):
                if i[index] in ". ":
                    domain = i[index+1 : n + 1]
                    visitCount[domain] += repeat
        lists = []
        for i,j in visitCount.items():
            lists.append(str(j) + " " + i)
        return lists
                
        