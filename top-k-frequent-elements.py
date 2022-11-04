class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        repeated = {}
        for i in range(len(nums)): repeated[nums[i]] = repeated.get(nums[i], 0) + 1
        lists = list(repeated.items())
        lists.sort(key = lambda i:i[1], reverse = True)
        ans = []
        for i in range(k): ans.append(lists[i][0])
        return ans
