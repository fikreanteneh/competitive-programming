class Solution:
    def maxLength(self, arr: List[str]) -> int:
        for i, val in enumerate(arr):
            arr[i] = Counter(val) 
        arr.sort()
        n = len(arr)
        self.length = 0
        letters = [0] * 26
        
        def helper(array):
            for i in array.values():
                if i > 1:
                    return False
            for i in array.keys():
                if letters[ord(i)-97]:
                    return False
            for i in array.keys():
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
                    for j in arr[i].keys():
                        letters[ord(j)-97] -= 1
        
        solution(0)
        return self.length
                
            
        