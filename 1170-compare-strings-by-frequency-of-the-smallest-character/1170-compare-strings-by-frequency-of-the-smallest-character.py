class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def helper(wordss):
            for i, word in enumerate(wordss):
                x = Counter(word)
                x = list(x.items())
                x.sort()
                wordss[i] = x[0][1]
        
        helper(queries)
        helper(words)
    
        words.sort()
        n = len(words)
        for i, val in enumerate(queries):
            index = bisect.bisect_right(words, val)
            queries[i] = n - index
        
        return queries
            
        
        