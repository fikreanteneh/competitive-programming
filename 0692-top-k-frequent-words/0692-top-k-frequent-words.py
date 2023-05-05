class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        words = Counter(words)
        words = list(words.items())
        for i, val in enumerate(words):
            words[i] = (-1 * val[1], val[0])
        heapify(words)
        ans = []
        for i in range(k):
            ans.append(heappop(words)[1])
        return ans