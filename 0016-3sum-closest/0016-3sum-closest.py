class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        i, j = 0, len(nums) - 1
        ans = float("inf")
        # print(nums)
        # while i < j:
        #     sums = nums[i] + nums[j]
        #     for k in range(0, len(nums)):
        #         check = sums + nums[k]
        #         if k == i or k == j:
        #             continue
        #         elif abs(check - target) < abs(ans - target):
        #             ans = check
        #         elif check == target:
        #             return check
        #     #     print(check)
        #     # print(nums[i], nums[j], ans)
        #     if sums < target:
        #         i += 1
        #     elif sums == target:
        #         break
        #     else:
        #         j -= 1
        # ans = float("inf")
        n = len(nums)
        for i, test in enumerate(nums):
            l, r = i + 1, n-1
            while l < r:
                sums = test  + nums[l] + nums[r]
                
                if abs(sums - target) < abs(ans - target):
                    ans = sums
                if sums == target:
                    return sums
                elif sums > target:
                    r -= 1
                else:
                    l += 1
        return ans
        