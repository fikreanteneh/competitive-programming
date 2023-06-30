class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nega, pos = [0]*(n//2), [0]*(n//2)        
        i1, i2 = 0, 0
        for i, num in enumerate(nums):
            if num < 0:
                nega[i1] = i
                i1 += 1
            else:
                pos[i2] = i
                i2 += 1
        answer = [0] * len(nums)
        for i in range(n//2):
            ind = 2 * i
            answer[ind] = nums[pos[i]]
            answer[ind + 1] = nums[nega[i]]
        return answer
        