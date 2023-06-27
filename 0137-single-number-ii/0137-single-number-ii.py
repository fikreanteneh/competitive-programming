class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        
        for i in range(32):
            bits = 0
            for num in nums:
                bits += (num >> i) & 1
            
            isOn = bits % 3
            answer |= (isOn << i)
        if answer >= 1 << 31:
             answer =  answer - (1 << 32) 
        
        return answer