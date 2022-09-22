class Solution:
    def maxArea(self, height: List[int]) -> int:
        max = 0
        i, j = 0, len(height)-1
        while i <= j:
            area = min(height[j],height[i]) * (j - i)
            if area > max: max = area
            if height[j] <= height[i]: j-=1
            else: i+=1
        return max
