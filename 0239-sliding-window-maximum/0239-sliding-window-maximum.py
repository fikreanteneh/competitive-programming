class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = deque([])
        nums.append(-10**5)
        for i in range(k - 1):
            while answer and answer[0] < nums[i]:
                answer.popleft()
            answer.appendleft(nums[i])
            # print(answer)
        ans = []
        for i in range(k - 1, len(nums) - 1):
            while answer and answer[-1] < nums[i - k]:
                answer.pop()
            if answer and answer[-1] == nums[i - k]:
                answer.pop()
            
            while answer and answer[0] < nums[i]:
                answer.popleft()
            answer.appendleft(nums[i])
            ans.append(answer[-1])
            # print(answer)
        return ans