class Solution:
    def insert(self, interval: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        stack = []
        n = len(interval)
        
        index = bisect_right(interval, newInterval)
        
        if index != 0 and interval[index - 1][0] <= newInterval[0] <= interval[index - 1][1]:
            newInterval[0] = interval[index - 1][0]
            index -= 1

        end = index 
        while end < n and interval[end][0] <= newInterval[1]:
            # print(interval[end], newInterval[1])
            newInterval[1] = max(interval[end][1], newInterval[1]) 
            end += 1
        # print(end)
        return interval[0:index] + [newInterval] + interval[end:]
    