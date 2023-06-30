class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
        answer = []
        stack = []
        n = len(s)
        def solution(index):
            if index >= n:
                if len(stack) == 4:
                    answer.append(".".join(stack))
                return
            for i in range(index, n):
                temp = s[index:i + 1]
                stack.append(temp)
                x = int(temp)
                if len(temp) == len(str(x))  and x < 256:
                    solution(i + 1)
                stack.pop() 
        solution(0)
        return answer
                