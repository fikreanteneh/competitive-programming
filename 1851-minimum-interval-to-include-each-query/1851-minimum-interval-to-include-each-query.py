class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        queries = sorted([(query, i) for i, query in enumerate(queries)])
        heap = []
        n = len(intervals)
        answer = [-1]*len(queries)
        index = 0
        for i, val in enumerate(queries):
            query, qIndex= val
            while index < n and query >= intervals[index][0]:
                heappush(heap,(intervals[index][1] - intervals[index][0] + 1, intervals[index][1]))
                index += 1
            while heap and heap[0][1] < query:
                heappop(heap)
            if heap:
                answer[qIndex] = heap[0][0]
        return answer
        #     # print(query)
        #     ans = float("inf")
        #     if i > 0 and query == queries[i - 1][0]:
        #         answer[index] = answer[ queries[i - 1][1]]
        #         continue
        #     # print(intervals)
        #     while intervals and query >= intervals[0][0]:
        #         curr = heappop(intervals)
        #         if (curr[1] < query):
        #             continue
        #         ans = min( ans, curr[2])
        #         heappush(intervals, (query + 1, curr[1], curr[2]))
        #     if ans != float("inf"):
        #         answer[index] = ans
        #     # print(intervals, ans)
        # return answer
                
        
        
#         def merge(left, right):
#             new = []
#             n, m = len(left), len(right)
#             i, j = 0, 0
#             while i < n and j < m:
#                 a, b, c = left[i][0], left[i][1], left[1] - left[0] 
#                 x, y, z = right[i][0], right[i][1], right[1] - right[0] 
#                 if b < x:
#                     new.append( (a, b, c))
#                     i += 1
#                 elif y < a:
#                     new.append( (x, y, z))
#                     j += 1
#                 elif a <= x <= b:
                    
        
        
#         def mergeSort(intervals):
#             n = len(intervals)
#             if n == 1:
#                 return intervals
#             left = mergeSort(intervals[:n//2])
#             right mergeSort(intervals[n//2:])
#             return merge(left, right)  
        # intervals = mergeSort(intervals)
    
#         stack = [ (0,0,0) ]
#         intervals.sort()
#         # print(intervals)
#         for a, b in intervals:
#             diff1 = b - a + 1
#             x, y, diff2 = stack[-1]
#             if a > y:
#                 stack.append( (a, b, diff1) )
#             elif b < y:
#                 stack[-1] = ( (x, a - 1, diff2)   )
#                 stack.append( (a,b, diff1) )
#                 stack.append ( (b, y, diff2)  )
#             elif diff2 > diff1:
#                 stack[-1] = (x, a, diff2)
#                 stack.append( (a, b, diff1) )
#             elif diff2 < diff1:
#                 stack.append( (y, b, diff1) )
#             # print(stack)
#         stack.append( (float("inf"), float("inf"), float("inf")))
#         # print(stack)
#         heapify(stack)
#         answer = [-1]*len(queries)
#         queries = sorted( [ query, i  for i, query in enumerate(queries)] )
#         for query, index in queries:
#             ans = float("inf")
#             while stack[0][1] < query:
#                 heappop(stack)
#             while 
            
            
        
        
#         for i, query in enumerate(queries):
#             index = bisect_left(stack, (query,query, 0)  )
#             ans = float("inf")
#             if stack[index - 1][0] <= query <= stack[index - 1][1]:
#                 ans = min(ans, stack[index - 1][2])
#             if stack[index][0] <= query <= stack[index][1]:
#                 ans = min(ans, stack[index][2])
#             if ans != float("inf"):
#                 answer[i] = ans
#         return answer
                
        
                
                
                
        