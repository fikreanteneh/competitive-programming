class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        store = set(nums)
        for i in nums:
            x = list(str(i))
            x.reverse()
            store.add(int("".join(x)))
        return len(store)