class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        n, m = len(s2), len(s1)
        if m > n:
            return False
        s1 = Counter(s1)
        check = Counter(s2[:m-1])
        for i in range(m-1, n):
            check[s2[i]] += 1
            # print(check)
            if check == s1:
                return True
            check[s2[i-m+1]] -= 1
        return False