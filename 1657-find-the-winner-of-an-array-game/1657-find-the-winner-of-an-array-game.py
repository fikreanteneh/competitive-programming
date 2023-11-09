class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        n = len(arr)
        arr = deque(arr)
        count = defaultdict(int)
        for _ in range(n):
            x, y = arr.popleft(), arr.popleft()
            x, y = min(x, y), max(x, y)
            arr.appendleft(y)
            arr.append(x)
            count[y] += 1
            if count[y] == k:
                return y
        return arr[0]