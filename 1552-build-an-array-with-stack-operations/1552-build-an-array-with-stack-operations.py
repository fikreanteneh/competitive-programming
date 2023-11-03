class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        target.reverse()
        answer = []
        for val in range(1, n + 1):
            answer.append("Push")
            if val == target[-1]:
                target.pop()
            else:
                answer.append("Pop")
            
            if not target:
                return answer
