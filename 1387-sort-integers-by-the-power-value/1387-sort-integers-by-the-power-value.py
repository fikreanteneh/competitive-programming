class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        
        store = {1: 0}
        def collatz(num):
            if num in store:
                return store[num]
            elif num % 2:
                ans = 1 + collatz( 3*num + 1)
            else:
                ans = 1 + collatz(num//2)
            store[num] = ans
            return ans
        
        answers = []
        for num in range(lo, hi + 1):
            answers.append( (collatz(num), num))
        answers.sort()
        return answers[k - 1][1]