class Solution:
    def maxLength(self, arr: List[str]) -> int:
        n = len(arr)
        self.length = 0
        self.let = set()
        def solution(index):
            self.length = max(self.length, len(self.let))
            for i in range(index, n):
                temp = set(list(arr[i]))
                if len(temp) == len(arr[i]) and not self.let.intersection(temp):
                    for lett in arr[i]:
                        self.let.add(lett)
                    solution(i + 1)
                    for lett in arr[i]:
                        self.let.discard(lett)
        solution(0)
        return self.length