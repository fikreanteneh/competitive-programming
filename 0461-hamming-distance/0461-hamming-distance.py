class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        ans = x ^ y
        return self.countBits(ans)
        
    def countBits(self, n: int) -> List[int]: 
            temp = n
            cur = 0
            checker = 1
            while temp:
                cur += (temp & 1)
                temp >>= 1
            return cur