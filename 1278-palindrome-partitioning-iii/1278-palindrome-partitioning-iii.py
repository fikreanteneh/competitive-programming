class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def costCalculate(string):
            cost = 0
            x = len(string)
            for i in range(x//2):
                if string[i] != string[x - i - 1]:
                    cost += 1
            return cost
        
        n = len(s)
        @cache
        def backtrack(index, div):
            if index == n:
                return 0 if div == k else float("inf")
            if div == k - 1:
                return costCalculate(s[index:])
            if div >= k:
                return float("inf")
            ans = float("inf")
            for i in range(index + 1, n + 1):
                subString = s[index : i]
                ans = min(ans, costCalculate(subString) + backtrack(i, div + 1))
            return ans
                
        
        return backtrack(0, 0)
        