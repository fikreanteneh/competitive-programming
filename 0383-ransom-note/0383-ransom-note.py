class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote = Counter(ransomNote)
        magazine = Counter(magazine)

        for i, j in ransomNote.items():
            if j > magazine[i]:
                return False
        
        return True