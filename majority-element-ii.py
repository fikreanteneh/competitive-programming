class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        check = {}
        for i in nums: check[i] = check.get(i, 0) + 1
        ans = []
        n = floor(len(nums)/3)
        for key in check:
            if check[key] > n: ans.append(key)
        return ans
