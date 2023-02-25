class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        store = { i for i in range(1, len(nums)+1)}
        for i in nums:
            store.discard(i)
        store = list(store)
        return store