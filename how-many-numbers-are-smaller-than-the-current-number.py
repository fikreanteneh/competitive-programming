class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        new = [0]*101
        for i in nums:
            new[i]+=1
        sum = 0
        for j in range(101):
            sum+=new[j]
            new[j]=sum-new[j]
        new2 = []
        for j in nums:
            new2.append(new[j])
        return new2
