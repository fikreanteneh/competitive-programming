class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        
        def findGCD(x, y) -> int:
            y, x = max(x,y), min(x, y)
            while True:
                temp = y % x
                if not temp:
                    return x
                y, x = x, temp
        n = len(nums) 
        ans = 0
        for i in range(n):
            gcd = nums[i]
            for j in range(i, n):
                gcd = findGCD(gcd, nums[j])
                if gcd == k:
                    ans += 1
                elif gcd < k:
                    break
        return ans
                