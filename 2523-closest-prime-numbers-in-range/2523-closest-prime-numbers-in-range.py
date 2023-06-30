class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        
        num = [True] * (right + 1)
        num[0], num[1] = False, False
        r = int(sqrt(right+1)) + 1
        for i in range(2, r):
            if num[i]:
                for j in range(i*i, right + 1, i):
                    num[j] = False
        
        ans = [-1, -1, float("inf")]
        curr = [float("inf"), float("inf")]
        index = 0
        for i in range(left, right + 1):
            if num[i]:
                curr[index] = i
                x = abs(curr[0] - curr[1])
                if x < ans[-1]:
                    ans[0], ans[1] = curr[0], curr[1]
                    if x <= 2:
                        break
                index = 1 - index
        ans.pop()
        ans.sort()
        return ans
        
            