class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        bags = [0 for i in range(k)]
        self.answer = float("inf")
        self.n = len(cookies)     
        if self.n == k:
            return max(cookies)
        def solution(index):
            if index == self.n:
                self.answer = min(self.answer, max(bags))
                return
            if max(bags) >= self.answer:
                return
            for i in range(k):
                bags[i] += cookies[index]
                solution(index + 1)
                bags[i] -= cookies[index]
        solution(0)
        return self.answer
    
    