class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        x = (num - 3)/ 3
        if x == int(x):
            return [ int(x), int(x) + 1, int(x) + 2 ]
        return []
        
        """
        y = x + x + 1 + x + 2
        y = 3X + 3
        y - 3 = 
        
        """