class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == "0":
            return 0
        answer = [0]* len(s)
        answer[-1] = 1 if s[-1] != "0" else 0
        answer.append(1)
        n = len(s)
        
        for i in range(n - 2, -1, -1):
            if s[i] != "0":
                answer[i] += answer[i + 1]
                if int(s[i:i+2]) <= 26:
                    answer[i] += answer[i + 2]
            # print(answer)
        
        
        return answer[0]