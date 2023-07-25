class Solution:
    @cache
    def climbStairs(self, n: int) -> int:
        array = [1, 1]
        for i in range(n - 1):
            array.append(array[-1] + array[-2])
        return array[-1]
        
        
        
        if n == 1:
            return 1
        elif n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)
        