class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        length = len(nums)
        list1 = [0]
        list2 = [0]
        for i in range(1, length):
            list1.append(list1[-1] + nums[i-1])
            list2.append(list2[-1] + nums[length - i])
        index = -1
        for i in range(length):
            if list1[i] == list2[length-1-i]: return i
        return -1
