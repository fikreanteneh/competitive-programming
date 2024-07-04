class Solution:
    def shortestSuperstring(self, words: List[str]) -> str:

        n = len(words)
        self.state = 0
        self.target = (1<<n) - 1
        
        def findPrefix(word1, word2):
            index = 0
            if word2 in word1:
                return ""
            m = len(word1)
            for i in range(min(len(word1),len(word2))):
                if word1[m - i - 1:] == word2[:i + 1]:
                    index = i + 1
            return word2[index:]
        
        store = [["" for i in range(n + 1)] for j in range(n + 1)]
        for i in range(n):
            for j in range(i):
                store[i][j] = findPrefix(words[i], words[j])
                store[j][i] = findPrefix(words[j], words[i])
        
        def pickTheBest(possible, curr):
            currBest = ("", float("inf"))
            for string, prev in possible:
                option = len(string) + len(store[prev][curr])
                if option < currBest[1]:
                    currBest = (string + store[prev][curr], option)
            return (currBest[0], curr)
        
        @cache
        def dp(state, curr):
            if (state ^ (1<<curr)) == self.target:
                return (words[curr], curr)
            state ^= (1 << curr)
            possible = []
            for i in range(n):
                if state & (1 << i):
                    continue
                possible.append(dp(state, i))
            return pickTheBest(possible, curr)
        
        answer = "x"*241
        for i in range(n):
            word, _ = (dp(0, i))
            if len(word) < len(answer):
                answer = word
        return answer
               
        
        
        
        #Subset Solution Does not work n!            
        def backtrack(curr, index):
            if len(curr) >= len(self.answer):
                return
            if self.state == self.target:
                if len(curr) < len(self.answer):
                    self.answer = curr
                return
            for i, word in enumerate(words):
                if self.state & (1 << i):
                    continue
                self.state ^= (1 << i)
                backtrack(curr + store[index][i], i)
                self.state ^= (1 << i)
        for i in range(n): 
            self.state = 1 << i
            backtrack(words[i], i)
        return self.answer
            