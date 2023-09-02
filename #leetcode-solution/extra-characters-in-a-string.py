class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        
        dictionary = set(dictionary)
        last = 0 if s[0] in dictionary else 1
        store = [0, last]
        for i in range(1, len(s)):
            mini = float("inf")
            for j in range(i + 1):
                word = s[j:i + 1]
                if word in dictionary:
                    mini = min(store[j], mini)
                else:
                    mini = min(mini, store[j] + i - j + 1)
            store.append(mini)
        
        
        return store[-1]
                    
                    