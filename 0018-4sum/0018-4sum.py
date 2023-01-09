class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
            unique_quadruplets = []
            nums.sort()
            n = len(nums)
            for i in range(n - 3):
                if i > 0 and nums[i] == nums[i - 1]:        # check for duplicates
                    continue
                for j in range(i + 1, n - 2):
                    if j > i + 1 and nums[j]== nums[j-1]:   # check for duplicates
                        continue
                    L, R = j + 1, n - 1    # left and right ptrs
                    while L < R:
                        s = nums[i] + nums[j] + nums[L] + nums[R]  # sum
                        if s == target:
                            unique_quadruplets.append([nums[i], nums[j], nums[L], nums[R]]) 
                            while L < R and nums[L] == nums[L+1]:  # check for duplicates
                                L += 1
                            while L < R and nums[R] == nums[R-1]:  # check for duplicates
                                R -= 1
                            L += 1
                            R -= 1
                        elif s < target:
                            L += 1
                        else:
                            R -= 1
            return unique_quadruplets