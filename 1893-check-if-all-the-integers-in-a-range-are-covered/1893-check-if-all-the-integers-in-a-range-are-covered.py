class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        answer = [False]*51
        for start, end in ranges:
            for i in range(start, end + 1):
                answer[i] = True
        return all(answer[left: right+1])