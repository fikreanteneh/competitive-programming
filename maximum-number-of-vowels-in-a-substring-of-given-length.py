class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        
        vowels = {"a","e","i","o","u"}
        repeat= maximum = 0
        
        for i in range(k-1): 
            if s[i] in vowels: repeat += 1
        j = 0
        for i in range(k-1, len(s)):
            if s[i] in vowels: repeat += 1
            maximum = max(maximum, repeat)
            if s[j] in vowels: repeat -= 1
            j += 1
        return maximum
                
