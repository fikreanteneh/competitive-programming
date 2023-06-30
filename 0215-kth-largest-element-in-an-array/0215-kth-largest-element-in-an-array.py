class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        check = len(nums) - k
        def quick(left, right):
            if left >= right:
                return nums[right]
            pivot = nums[left]
            # print(left, right, "-----", check)
            write = left + 1
            for read in range(left + 1, right + 1):
                # print(nums[read], "-", write)
                if nums[read] <= pivot:
                    nums[read], nums[write] = nums[write], nums[read]
                    write += 1
                # print("-", write)
            
            nums[write-1], nums[left] = nums[left], nums[write -1]
            # print(nums, write - 1)
            if write - 1 == check:
                return nums[write -1]
            elif write - 1 < check:
                return quick(write, right)
            else:
                return quick(left, write - 2)
        
        return quick(0, len(nums)-1)
            