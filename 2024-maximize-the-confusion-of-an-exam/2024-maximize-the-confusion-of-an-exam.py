class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)
        def solve(char):
            answer = 0
            left = 0
            notEqual = 0
            for right, curr in enumerate(answerKey):
                if curr != char:
                    notEqual += 1
                while left < right and notEqual > k:
                    if char != answerKey[left]:
                        notEqual -= 1
                    left += 1
                answer = max(answer, right - left + 1)
            return answer
        
        return max(solve("T"), solve("F"))
                    
            