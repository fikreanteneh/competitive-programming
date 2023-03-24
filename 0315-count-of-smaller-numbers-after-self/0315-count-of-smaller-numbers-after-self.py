class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        for i, val in enumerate(nums):
            nums[i] = (val, i)
        n = len(nums)
        temp = [None] * n
        self.answer = [0] * n
        
        
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
            stack = [0] * (mid - left)
            while i < mid and j < right:
                if nums[j][0] < nums[i][0]:
                    stack[i - left] += 1
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
            curr = 0
            for i in range(left, mid):
                curr += stack[i-left]
                self.answer[nums[i][1]] += curr
            for i in range(left, right):
                nums[i] = temp[i]
        
        mergeSort(0, n - 1)
        return self.answer