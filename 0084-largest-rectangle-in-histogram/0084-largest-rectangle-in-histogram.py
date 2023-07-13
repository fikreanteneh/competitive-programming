class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = [(-1, -1)]    
        answer = 0
        for i, val in enumerate(heights):
            while stack[-1][0] > val:
                height, index = stack.pop()
                width = i - stack[-1][1] - 1
                answer = max(answer, height * width)            
            stack.append((val,i))       
        return answer    
