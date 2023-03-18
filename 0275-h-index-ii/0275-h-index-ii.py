class Solution:
    def hIndex(self, citations: List[int]) -> int:
        left = 0
        right = len(citations) - 1
        n = len(citations)
        answer = 0
        while left <= right:
            mid = left + (right-left) // 2
            
            if n - mid <= citations[mid]:
                answer = max(answer, n - mid)
                right = mid - 1
            else:
                left = mid + 1
        return answer
    