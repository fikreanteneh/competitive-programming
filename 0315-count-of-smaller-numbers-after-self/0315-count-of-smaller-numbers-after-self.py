class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        for i, val in enumerate(nums):
            nums[i] = (val, i)
        n = len(nums)
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
            temp = []
            stack = [0] * (mid - left)
            while i < mid and j < right:
                if nums[j][0] < nums[i][0]:
                    stack[i - left] += 1
                    temp.append(nums[j])
                    j += 1
                else:
                    temp.append(nums[i])
                    i += 1
            temp.extend(nums[i:mid])
            temp.extend(nums[j:right])
            curr = 0
            for i in range(left, mid):
                curr += stack[i-left]
                self.answer[nums[i][1]] += curr
            for i in range(left, right):
                nums[i] = temp[i - left]
        
        mergeSort(0, n - 1)
        return self.answer