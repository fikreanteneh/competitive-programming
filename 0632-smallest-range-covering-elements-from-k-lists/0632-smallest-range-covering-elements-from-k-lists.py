class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        n = len(nums)
        if n == 1:
            return [nums[0][0], nums[0][0]]
        interval = [float("inf"), float("-inf")]
        for i, val in enumerate(nums):
            nums[i] = (val[0], 0, val)
            interval[1] = max(interval[1], val[0])
        heapify(nums)
        answer = [float("-inf"), float("inf")]
        while len(nums) == n:
            leading, index, arr = heappop(nums)
            index += 1
            interval[0] = min(nums[0][0], leading)
            
            if interval[1] - interval[0] < answer[1] - answer[0]:
                answer = interval.copy()
            
            if index < len(arr):
                interval[1] = max(interval[1], arr[index])
                heappush(nums, (arr[index], index, arr))
        
        return answer
        
            