class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        stack = []
        answer = 0
        for right in range(n):
            rightBlock = height[right]
            while stack and stack[-1][0] <= height[right]:
                middleBlock, middle = stack.pop()
                if not stack:
                    continue
                leftBlock, left = stack[-1]
                answer += (  min(leftBlock - middleBlock, rightBlock - middleBlock)*(right - left -1))
            stack.append( (height[right], right) )
        return answer
                
            