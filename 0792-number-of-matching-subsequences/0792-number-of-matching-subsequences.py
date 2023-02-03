class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        ans = 0
        checker = defaultdict(list)
        for i, lett in enumerate(s):
            checker[lett].append(i)
        for word in words:
            index = -1
            flag = True
            for i, lett in enumerate(word):
                index = bisect.bisect_left(checker[lett], index + 1)
                if index == len(checker[lett]):
                    flag = False
                    break
                index = checker[lett][index]
            if flag:
                ans += 1
        return ans
                
        
#         def checker(temp, check):
#             for k in temp:
#                 if k not in check or temp[k] != check[k]:
#                     return False
#             return True
#         ans = 0
#         check = {}
        
#         temp = {}
#         for i in range(len(s)-1, -1,-1 ):
#             check[s[i]] = temp.copy()
#             temp[s[i]] = temp.get(s[i], 0) + 1
#         # print(check)
#         for i in words:
#             temp2 = {}
#             flag = True
            
#             for j in range(len(i)-1, -1, -1):
#                 if i == "bb":
#                     print(temp2, check[s[j]])
#                 if not checker(temp2, check[s[j]]):
#                     flag = False
#                     break
#                 if i == "bb":
#                     print(temp2, check[s[j]])
#                 temp2[s[j]] =  temp2.get(s[j], 0) + 1
#                 if i == "bb":
#                     print(temp2, check[s[j]])
    
#             if flag:
#                 ans += 1
#         return ans
                
            
                    
                        