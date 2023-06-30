class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        temp = [None] * n
        
        def mergeSort(left, right):
            if left >= right:
                return
            mid = left + (right - left) // 2
            mergeSort(left, mid)
            mergeSort(mid + 1, right)
            merge(left, mid + 1 ,right + 1) 
                    
        def merge(left, mid ,right):
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
        
        mergeSort(0, n - 1)
        return nums