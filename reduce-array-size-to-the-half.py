class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        repeated = list(Counter(arr).items())
        n = len(arr)//2
        repeated.sort(key=lambda x: x[1])
        print(repeated)
        sum = 0
        for i in range(len(repeated)-1,-1,-1):
            sum += repeated[i][1]
            if sum >= n: return len(repeated) - i
