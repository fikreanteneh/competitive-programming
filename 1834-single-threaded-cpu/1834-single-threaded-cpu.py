class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, val in enumerate(tasks):
            tasks[i] = (val[0], val[1], i)
        tasks.sort()
        pq = []
        ans = []
        i = 0
        n = len(tasks)
        t = tasks[0][0]
        while i < n or pq:
            while i < n and tasks[i][0] <= t:
                heappush(pq, (tasks[i][1], tasks[i][2])) 
                i += 1
            if pq:
                curTime, index = heappop(pq)
                ans.append(index)
                t += curTime
            else:
                t = tasks[i][0]
        return ans
        