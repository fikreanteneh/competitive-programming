class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        ans = Counter(arr)
        return len(ans.values()) == len(set(ans.values()))
    