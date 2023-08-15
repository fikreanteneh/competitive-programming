class Solution:
    def minimumDistance(self, word: str) -> int:
        # self.f1 = None
        # self.f2 = None
        # self.answer = 0
        letter = {chr(i + ord("A")): (i//6, i%6) for i in range(26)}
        n = len(word) - 1
        @cache
        
        def sol(index, f1, f2):
            nextt = letter[word[index]]
            left = 0 if not f1 else (abs(f1[0] - nextt[0]) + abs(f1[1] - nextt[1]) )
            right = 0 if not f2 else (abs(f2[0] - nextt[0]) + abs(f2[1] - nextt[1]) )
            if index == n:
                return min(left, right)
            left += sol(index + 1, nextt, f2)
            right += sol(index + 1, f1, nextt)
            return min(left, right)
        return sol(0, letter[word[0]], None)
            
            
        