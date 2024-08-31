class Solution:
    def subarrayBitwiseORs(self, arr: List[int]) -> int:
        bitwisePrefix = arr[0]
        result = set()
        prevPrefix = set()
        for num in arr:
            prevPrefix = set([num | prefix for prefix in prevPrefix])
            prevPrefix.add(num)
            result.update(prevPrefix)
        return len(result)