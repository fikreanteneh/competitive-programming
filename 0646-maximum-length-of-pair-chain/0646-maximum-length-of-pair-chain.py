class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort()
        n = len(pairs)
        answer = [1]
        
        for i in range(1, n):
            most = 0
            for j in range(i - 1, -1, -1):
                if pairs[i][0] > pairs[j][1]:
                    most = max(most, answer[j])
            answer.append(most + 1)
        
        return max(answer)
                