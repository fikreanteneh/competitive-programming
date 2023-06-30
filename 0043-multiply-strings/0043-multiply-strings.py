class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        """      
        
        """
        numbers = {str(num) : num for num in range(10)}
        x = y = 0
        for i in num1:
            x = x * 10 + numbers[i]
        for i in num2:
            y = y * 10 + numbers[i]
        result = x * y
        return str(result)
        
                
                
                