class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        store = [(1, 0, 0)]
        maxi = (1, 0, 0)
        for i in range(1,len(nums)):
            num = nums[i]
            store.append((1, i, i))
            for j in range(i - 1, -1, -1):
                if num % nums[j] == 0 and (store[i][0]==1 or store[i][0]-1 < store[j][0]) :
                    store[i] = (1 + store[j][0] , j, i)
            if store[i][0] > maxi[0]: maxi = (store[i][0], store[i][1], i)
        ans, index = [], maxi[1]
        while maxi[1] != maxi[2]:
            ans.append(nums[maxi[2]])
            maxi = store[maxi[1]]
        ans.append(nums[maxi[2]])
        return ans
