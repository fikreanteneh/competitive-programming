class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        i = 0
        nums.sort()
        for j in range(len(nums)):
            k += nums[j]
            if k < nums[j] * (j - i + 1):
                k -= nums[i]
                i += 1
        return j - i + 1
        # print(len(nums))
        # nums.sort()
        # nums.reverse()
        # prefix = [0]
        # prefix = [nums[0] - nums[i] for i in range(1, len(nums))]
        # prefix.append(prefix[-1])
        # print(len(prefix))
        # i, j = 0, 1
        # ans = 0
        # sums = 0
        # while j < len(prefix):
        #     sums += (prefix[j] - prefix[i])
        #     if sums <= k:
        #         ans = max(ans, j - i)
        #         j += 1  
        #     else:
        #         sums -=(prefix[i+1] * (j-i+1))
        #         i += 1
        #     print(sums)
        # return ans
    """
    13, 8, 4, 1
    0  5  4   3
    0  5  9   12
    
    """