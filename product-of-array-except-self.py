class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        list1 = [1] * length
        list2 = [1] * length
        product1, product2 = 1, 1
        for i in range (1,length):
            product1 = list1[i - 1]*nums[i - 1]
            list1[i] = product1
            product2 = list2[length - i] * nums[length - i]
            list2[length - i -1] = product2
        new = []
        for i in range(length):
            new.append(list1[i]*list2[i])
        return new
