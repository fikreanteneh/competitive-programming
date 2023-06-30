class Solution:
    def similarPairs(self, words: List[str]) -> int:
        main = {}
        answer = 0
        for i in words:
            x = list(Counter(i))
            x.sort()
            x = tuple(x)
            main[x] = main.get(x, 0) + 1
            answer += (main[x] - 1)
        return answer
                
            
        