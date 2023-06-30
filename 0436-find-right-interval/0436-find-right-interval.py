class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        
        
        for i, val in enumerate(intervals):
            intervals[i] = (tuple(val), i)
        intervals.sort() #key = lambda x : x[0][1] 
        
        n = len(intervals)
        answer = [-1] * n
        
        for interval in intervals:
            left, right = 0, n - 1
            check = interval[0][1]
            mini = float("inf")
            while left <= right:
                mid = left + (right - left) // 2
                if check == intervals[mid][0][0]:
                    answer[interval[1]] = intervals[mid][1]
                    break
                elif check > intervals[mid][0][0]:
                    left = mid + 1
                else:
                    if mini > intervals[mid][0][0]:
                        mini = intervals[mid][0][0]
                        answer[interval[1]] = intervals[mid][1]
                    right = mid - 1
        return answer