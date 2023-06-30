class Solution:
    def distinctPrimeFactors(self, nums: List[int]) -> int:
        stack  = set()
        for num in nums:
            while num > 1:
                n = num // 2
                while num % n != 0:
                    n -= 1
                stack.add(num // n)
                num = n
        
        return len(stack)
        