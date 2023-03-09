class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        answer = set()
        temp = []
        n += 1
        
        def solution(curr):
            temp.append(curr)
            length = len(temp)
            if length >= k:
                # answer.append(temp[length - k : length])
                answer.add(tuple(temp[length - k : length]))
            if curr == n - 1:
                return
            for i in range(curr + 1, n):
                solution(i)
                temp.pop()
                
        solution(1)
        # answer.sort()
        # print("--",)
        # answer.pop()
        return list(answer)