class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i, num in enumerate(nums):
            nums[i] = num % 2
        cache = defaultdict(int)
        cache[0] = 1
        sum = 0
        count = 0
        for num in nums:
            sum += num
            count += cache[sum-k]
            cache[sum] += 1
        return count
            
#         n = len(nums)
#         sums = 0
#         for i, num in enumerate(nums):
#             sums = (num % 2) + sums
#             nums[i] = sums
#         ans = left = right = i = j = 0
#         print(nums)
#         while right < n:
            
#             first = nums[j]
#             while right < n-1 and nums[right+1] == first:
#                 right += 1
                
#             check1 = right - j + 1
            
#             right += 1
#             j = right
            
#             second = first - k
#             print(second)
#             if second == 0 and nums[0] != 0:
#                 ans += (check1 * 1)
#             elif second >= 0:
#                 while nums[left + 1] < second:
#                     left += 1
#                 print(i, left)
#                 i = left
#                 third = nums[left]
#                 while left < n and nums[left] == second:
#                     left += 1
#                 print(left)
#                 check2 = left - i
#                 left = left 
#                 ans += (check1 * check2)
#             print("ans",ans)
        
        # for right in range(n):
        #     sums += nums[right]
        #     nums[right]
        
        # 0 0 0 1 1 1 2 2 2 2 
        
        return ans