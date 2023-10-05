class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr, count = float("inf"), 0
        for num in nums:
            # print(curr, count, "-----", num)
            if count == 0:
                curr = num
                count = 1
            elif curr == num:
                count += 1
            else:
                count -= 1
        total = 0
        for num in nums:
            if num == curr:
                total += 1
        return curr