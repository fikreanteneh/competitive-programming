class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # 8
        value_index_dict = dict()
        for i, num in enumerate(nums):
            diff = target - num
            if diff in value_index_dict:
                return [value_index_dict[diff], i]
            value_index_dict[num] = i
            # Test 17
