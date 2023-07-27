class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        wordLength = len(words[0])
        n = len(s)
        m = len(words)
        collection = Counter(words)
        self.total = 0
        answer = set()
        
        def moveLeftPointer(left, right, word):
            temp =""
            while left < right and word != temp:
                temp = s[left: left + wordLength]
                if temp in collection:
                    words[temp] += 1
                    self.total -=1
                left += wordLength
            return left
            
        for start in range(wordLength):
            left, right = start, start
            bound = 0
            words = collection.copy()
            while left < n and right + wordLength <= n:
                word = s[right : right + wordLength]
                if word not in collection:
                    left = moveLeftPointer(left,right + wordLength, word)
                    right = left
                elif words[word] <= 0:
                    left = moveLeftPointer(left,right, word)
                else:
                    words[word] -= 1
                    self.total += 1
                    right += wordLength
                bound = (right - left) // wordLength
                if bound == m:
                    answer.add(left)
                    left = moveLeftPointer(left, left + wordLength, s[left: left + wordLength])
        return answer
                
            
                
        
        