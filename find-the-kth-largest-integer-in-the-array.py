class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        new = []
        for i in nums:
            new.append(int(i))
        new.sort()
        return str(new[len(new)-k])
