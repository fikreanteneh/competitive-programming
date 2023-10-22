class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        heap = [ (-nums[0], 0) ]
        answer = nums[0]
        for i in range(1,len(nums)):
            while i - heap[0][1] > k:
                heappop(heap)
            curr = max( nums[i], nums[i] - heap[0][0])
            answer = max(curr, answer)
            heappush(heap, (-curr, i ) )
        return answer