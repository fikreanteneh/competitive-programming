class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shift = [0] * (len(s) + 1)
        for start, end, dire in shifts:
            if dire == 0: dire = -1
            shift[start] += dire
            shift[end + 1] -= dire
        sums = 0
        for i in range(len(shift)-1):  
            shift[i] += sums
            sums = shift[i]
            ind = ord(s[i]) - 97 + sums
            if ind < 0: ind = 26 + (ind % (-26))
            if ind >= 26: ind %= 26
            shift[i] = chr(ind + 97)
        shift.pop()
        return "".join(shift)
