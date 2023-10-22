class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        answer = nums[k]
        left = right = k
        c = 1
        n = len(nums)
        curr = nums[k]
        while c < n:
            if left > 0 and (right == n - 1 or nums[left - 1] >= nums[right + 1]):
                left -= 1
            else:
                right += 1
            curr = min(curr, nums[right], nums[left])
            answer = max(answer, curr*(right - left + 1) )
            c += 1
        return answer
        
        # If we consider any subarray
            
#         answer = 0
#         for i in range(len(nums)):
#             val = nums[i]
#             j = i
#             while stack and stack[-1][0] > val:
#                 val2, j = stack.pop()
#                 if j > k:
#                     continue
#                 answer = max(answer, (i - j)*val2 )
#             stack.append( (val, j) )
#             if j > k:
#                 continue
#             answer = max(answer, (i - j + 1)*val )
#         for val, index in stack:
#             if not (index <= k <= stack[-1][1]):
#                 break
#             answer = max(answer, (stack[-1][1] - index  + 1)*val)
#         return answer