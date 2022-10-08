class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        subarrays = sum = 0
        for i in range(k-1): sum += arr[i]
        i = 0
        for j in range(k-1, len(arr)):
            sum += arr[j]
            if sum/k >= threshold: subarrays += 1
            sum-=arr[i]
            i += 1
        return subarrays
