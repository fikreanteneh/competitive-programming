class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        arr = [0] * 102
        for i in nums:
            arr[i + 1] += 1
        ans = []
        for i in range(1,102):
            arr[i] = arr[i-1] + arr[i]
        for i in nums:
            ans.append(arr[i])
        return ans