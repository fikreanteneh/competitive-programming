class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        store = defaultdict(int)
        words.sort(key = lambda x: len(x))
        for word in words:
            curr = 0
            for i in range(len(word)):
                check = word[0: i] + word[i + 1:]
                curr = max(curr, store[check])
            store[word] = curr + 1
        
        return max(store.values())