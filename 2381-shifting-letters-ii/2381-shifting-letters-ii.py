class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        shifting = [0] * (n + 1)
        for shift in shifts:
            shift[2] = -1 if shift[2] == 0 else 1
            shifting[shift[0]] += shift[2]
            shifting[shift[1] + 1] -= shift[2]
        
        ans = []
        shi = 0
        
        for i in range(n):
            
            shi += shifting[i]
            index = (ord(s[i]) - 97) + shi
            index = index % 26
            if index < 0:
                index += 26
            shifting[i] = chr(index + 97)
            
        shifting.pop()
        
        return "".join(shifting)
        