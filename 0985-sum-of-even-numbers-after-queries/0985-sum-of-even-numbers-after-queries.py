class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sums = 0
        for i in nums:
            if i % 2 == 0:
                sums += i
        answer = [0] * len(queries)
        for j, i in enumerate(queries):
            numsPairty = nums[i[1]] % 2
            queryPairty = i[0] % 2
            if queryPairty == 1 and numsPairty == 1:
                sums += (i[0] + nums[i[1]])
            elif queryPairty == 1 and numsPairty == 0:
                sums -= nums[i[1]]
            elif queryPairty == 0 and numsPairty == 0:
                sums += i[0]
            nums[i[1]] += i[0]
            answer[j] = sums
        return answer