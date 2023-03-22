class Solution:
    def maxLength(self, arr: List[str]) -> int:
        maxi = 0
        for i in arr:
            maxi += len(i)
        maxi %= 26
        n = len(arr)
        self.length = 0
        letters = [0] * 26
        
        def helper(array):
            count = Counter(array)
            for i in count.values():
                if i > 1:
                    return False
            for i in count.keys():
                if letters[ord(i)-97]:
                    return False
            for i in count.keys():
                letters[ord(i)-97] += 1
            return True
        
        def solution(index):
            if index >= n:
                self.length = max(self.length, sum(letters))
                return
            for i in range(index, n):
                temp = helper(arr[i])
                solution(i + 1)
                if temp:
                    for j in arr[i]:
                        letters[ord(j)-97] -= 1
        
        solution(0)
        return self.length
                
        
        
        
        
#         def repeated(val):
#             x = Counter(val)
#             for i in x.values():
#                 if i > 1:
#                     return set()
#             return set(x.keys())
        
#         length = 0
#         for i, val in enumerate(arr):
#             store = repeated(val)
#             if not repeated:
#                 continue
#             for j in range(i+1, len(arr)):
#                 vals = repeated(arr[j])
#                 if not vals:
#                     continue
#                 if not len(store.intersection(vals)):
#                     store = store.union(vals)
#             print(len(store))
#             length = max(length, len(store))  
#         return length
            
        