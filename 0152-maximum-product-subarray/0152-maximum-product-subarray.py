class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        lastNegative = 1
        answer = float("-inf")
        product = 1
        left = 0
        n = len(nums)
        for i, num in enumerate(nums):
            product *= num
            answer = max(answer, product, product//lastNegative)
            if product < 0 and lastNegative == 1:
                lastNegative = product
            if num == 0:
                lastNegative = 1
                product = 1
        
        return answer