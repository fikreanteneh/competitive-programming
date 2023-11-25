class Solution:
    def getSumAbsoluteDifferences(self, arr: List[int]) -> List[int]:
            prefix = [0]
            n = len(arr)
            for val in arr:
                prefix.append(prefix[-1] + val)
            answer = [0]*n
            for i in range(1, n + 1):
                left = arr[i - 1]*(i - 1) - prefix[i - 1]
                right =  (prefix[-1] - prefix[i]) - (arr[i - 1]*(n - i))
                answer[i - 1] = left + right
            return answer