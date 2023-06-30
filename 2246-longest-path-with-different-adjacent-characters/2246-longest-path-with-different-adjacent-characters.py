class Solution:
    def longestPath(self, parent: List[int], s: str) -> int:
        n = len(s)
        graph = defaultdict(list)
        self.maxi = 1
        for i, val in enumerate(parent):
            graph[val].append(i)
        
        def solution(node):  
            
            maxi = [float("-inf"), float("-inf")]
            letter = s[node]
            
            for child in graph[node]:
                childLetter = solution(child)
                if childLetter[1] != letter:
                    if childLetter[0] > maxi[0]:
                        maxi[1] = maxi[0]
                        maxi[0] = childLetter[0]
                    elif childLetter[0] > maxi[1]:
                        maxi[1] = childLetter[0]
            
            self.maxi = max(self.maxi, 1 + maxi[0], 1, sum(maxi) + 1)
            # if node == 0:
            #     print(maxi)
            #     print(self.maxi)
            return (max(1, maxi[0] + 1), letter)
            
        
        solution(0)
        return self.maxi
        
#         def compare(paths, list2):
#             maxi = Counter(list2)[True]
#             for path in paths:
#                 curr = 0
#                 for i, val in enumerate(path):
#                     if list2[i] and val:
#                         curr = 0
#                         break
#                     if val:
#                         curr += 1
#                 maxi = max(maxi, curr + maxi)
#             return maxi
        
#         def solution(node):
#             letter = ord(s[node]) - 97
#             temp = [False] * 26
#             temp[letter] = True
#             paths = []
#             curr = 0
#             for child in graph[node]:
#                 childLetters = solution(child)
                
#                 for childLetter in childLetters:
#                     if not childLetter[letter]:
#                         x = compare(paths, childLetter) + 1
#                         self.maxi = max(self.maxi, x)
#                         curr = max(curr, x)
#                         paths.append(childLetter)
            
#             for path in paths:
#                 path[letter] = True
#                 if node == 1:
#                     print(path)
#             paths.append(temp)
#             if node == 1:
#                 print(path)
#                 print(curr)
#                 print(self.maxi)
#             return paths
            
        
        
                    
        