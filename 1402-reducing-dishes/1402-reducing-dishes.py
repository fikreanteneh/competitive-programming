class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)
        if satisfaction[0] <= 0:
            return 0
        # print(satisfaction)
        curr = 0
        prev = 0
        newCurr = 0
        index = 0
        while index < len(satisfaction) and curr >= newCurr:
            prev +=satisfaction[index]
            newCurr, curr = curr, curr + prev
            index += 1
            # print(curr, newCurr)
        return max(curr, newCurr)
            
        