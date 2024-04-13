class Solution:
    def findIntegers(self, n: int) -> int:
        binary = bin(n)[2:]
        store = [1,1]
        for i in range(len(binary)):
            store.append(store[-2] + store[-1])
        answer = 1
        last = 0
        for i in range(len(binary) - 1, -1, -1):
            if n&(1 << i):
                answer += store[i + 1]
                if last == 1:
                    answer -= 1
                    break
                last = 1
            else:
                last = 0
        return answer
                
        
            
        
        