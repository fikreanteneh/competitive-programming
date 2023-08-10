class Solution:
    def countAndSay(self, n: int) -> str:
                
        
        def solution(num):
            i = 0
            n = len(num)
            ans = []
            while i < n:
                char = num[i]
                j = i
                while j < n and num[j] == char:
                    j += 1
                ans.append(str(j - i))
                ans.append(char)
                i = j
            return "".join(ans)
                
        answer = "1"
        for _ in range(1,n):
            answer = solution(answer)
        return answer