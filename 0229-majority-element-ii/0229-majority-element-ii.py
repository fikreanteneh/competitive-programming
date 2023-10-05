class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        majority = n//3
        curr1, count1 = float("inf"), 0
        curr2, count2 = float("inf"), 0
        for num in nums:
            # print(curr1, count1)
            # print(curr2, count2)
            if curr1 == num: count1 += 1
            elif curr2 == num: count2 += 1
            elif count1 == 0:
                curr1, count1 = num, 1
                # curr1 = num
            elif count2 == 0:
                curr2, count2 = num, 1
                # curr2 = num
            else:
                count1 -= 1
                count2 -= 1
        #     print()
        # print(curr1, count1)
        # print(curr2, count2)
        total1, total2 = 0, 0
        for num in nums:
            if num == curr1:
                total1 += 1
            elif num == curr2:
                total2 += 1
        answer = []
        if total1 > majority:
            answer.append(curr1)
        if total2 > majority:
            answer.append(curr2)
        return answer
     