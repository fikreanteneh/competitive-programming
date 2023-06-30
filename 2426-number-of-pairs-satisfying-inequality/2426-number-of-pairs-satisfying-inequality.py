class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], diff: int) -> int:
        n = len(nums1)
        for i in range(n):
            nums1[i] = nums1[i] - nums2[i]
        nums = nums1
        # print(nums)
        self.ans = 0
        temp = [None] * n
        def mergeSort(left, right):
            if left >= right:
                return
            mid = left + (right - left) // 2
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            merge(left, mid + 1 ,right + 1)
        
        def count(left,mid, right):
            for i in range(mid, right):
                target = nums[i] + diff
                
                x = bisect_right(nums, target, left, mid)
                # print(x, left,"tar--", target, x - left)
                self.ans += (x - left)
            # i, j = left, mid
            # while i < mid and j < right:
            #     target = nums[j] + diff
            #     if nums[i] <= nums[j]:
            #         if nums[i] <= target:
            #             self.ans += (mid - i)
            #         j += 1
            #     else:
            #         i += 1      
        def merge(left, mid ,right):
            count(left, mid, right)
            # print(nums[left:mid], nums[mid:right], self.ans)
            i, j = left, mid
            index = left
            while i < mid and j < right:
                if nums[j] <= nums[i]:
                    temp[index] = nums[j]
                    j += 1
                else:
                    temp[index] = nums[i]
                    i += 1
                index += 1

            while i < mid:
                temp[index] = nums[i]
                i += 1  
                index += 1
            while j < right:
                temp[index] = nums[j]
                j += 1
                index += 1
            for i in range(left, right):
                nums[i] = temp[i]
        mergeSort(0, n-1)
        return self.ans
        
            