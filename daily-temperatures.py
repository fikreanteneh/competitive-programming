class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        for a in range (len(temperatures)):
            i = temperatures[a]
            while stack and stack[-1][0] < i:
                temperatures[stack[-1][1]] = a - stack[-1][1]
                stack.pop()
            stack.append((i,a))
        for i in stack:
            temperatures[i[1]] = 0 
        return temperatures
