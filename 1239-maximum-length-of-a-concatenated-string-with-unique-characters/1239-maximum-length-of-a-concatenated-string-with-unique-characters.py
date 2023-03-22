class Solution:
    def maxLength(self, arr: List[str]) -> int:
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
                
            
        