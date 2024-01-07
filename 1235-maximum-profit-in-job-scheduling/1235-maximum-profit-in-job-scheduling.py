class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        n = len(startTime)
        for i in range(n):
            startTime[i] = (startTime[i], endTime[i] , profit[i])
        startTime.sort()
        @cache
        def dp(index):
            if index >= n:
                return 0
            start, end, pro = startTime[index]
            nextt = bisect_left(startTime, (end, end))
            pro += dp(nextt)
            return max(pro, dp(index + 1))
        answer = 0
        for i in range(n):
            answer = max( answer, dp(i))
        return answer
                                            
            
            