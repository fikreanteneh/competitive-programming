class Solution:
    def createSortedArray(self, instructions: List[int]) -> int:
        cost = 0
        answer = [0] * 100001
        
        def sums(val):
            total = 0
            while val > 0:
                total += answer[val]
                val -= (val & -val)
            return total            
            
        def update(val):
            while val <= 100001:
                answer[val] += 1
                val += (val & -val)
            
        for i, val in enumerate(instructions):
            before = sums(val - 1)
            after = i - sums(val)
            cost += min(before, after)
            update(val)
        return cost % (10**9 + 7)
            
            
        
        
        