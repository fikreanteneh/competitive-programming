class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        n = len(words)
        letters = Counter(letters)
        visited = set()
        
        def contain(word):
            point = 0
            flag = False
            for letter in word:
                if letters[letter] == 0:
                    flag = True  
                point += score[ord(letter) - ord("a")]
                letters[letter] -= 1
            if flag:
                return (False, 0)
            return (True, point)
            
            
        def uncontain(word):
            for letter in word:
                letters[letter] += 1
        
        def dfs(prev):
            ans = prev
            for i in range(n):
                if i not in visited:
                    visited.add(i)
                    possible, point = contain(words[i])
                    if possible :   
                        ans = max(ans, dfs(point + prev), point + prev)
                    uncontain(words[i])
                    visited.discard(i)
            return ans
        
        return dfs(0)