class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionry = {}
        # for i in range(len(nums)):
        #     if target - nums[i] in dictionry:
        #         return [dictionry[target - nums[i]], i]
        #     dictionry[nums[i]] = i
        
    # Create a dictionary to store the value and index of each element in the array
        value_index_dict = {}
    
    # Iterate through the array
        for i, num in enumerate(nums):
            # Calculate the difference between the target and the current element
            diff = target - num

            # If the difference is in the dictionary, then we have found the two elements that add up to the target
            if diff in value_index_dict:
                return [value_index_dict[diff], i]

            # Otherwise, add the current element and its index to the dictionary
            value_index_dict[num] = i
