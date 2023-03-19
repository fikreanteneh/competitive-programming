class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        answer = {()}
        stack = []
        self.n = len(nums)
        
        def solution(index):
            if index == self.n:
                return
            stack.append(nums[index])
            for i in range(len(stack)):
                answer.add( tuple(stack[i:]))
            for i in range(index + 1, self.n):
                solution(i)
                stack.pop()  
        solution(0)
        return list(answer)
         