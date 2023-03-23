class Solution:
    def maximumRequests(self, n: int, requests: List[List[int]]) -> int:
        build = [0] * n
        n = len(requests)
        self.maxi = 0
        def solution(index, total):   
            if not any(build):
                self.maxi = max(self.maxi, total)      
            for i in range(index, n ):
                request = requests[i]
                build[request[0]] -= 1
                build[request[1]] += 1
                solution(i + 1, total + 1)
                build[request[0]] += 1
                build[request[1]] -= 1
        solution(0,0)
        return self.maxi
                    