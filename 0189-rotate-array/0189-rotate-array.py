class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= len(nums): k = k % (len(nums))
        new = []
        for i in range(k):
            new.append(nums[i - k])
        new= new + nums[:0-k]
        for j in range(len(new)):
            nums[j] = new[j]