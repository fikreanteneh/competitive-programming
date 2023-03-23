class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        
        answer = set()
        stack = [float("-inf")]
        n = len(nums)
        
        def solution(index):
            if len(stack) > 2:
                answer.add(tuple(stack[1:]))
            if index >= n:
                return
            for i in range(index, n):
                stack.append(nums[i])
                if stack[-1] >= stack[-2]:
                    solution(i+1)
                stack.pop()

        solution(0)
        return answer
                    