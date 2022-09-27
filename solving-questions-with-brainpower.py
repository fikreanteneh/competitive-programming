class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        maximum = 0
        leng = len(questions)
        new = [None]*leng
        for i in range(leng-1,-1,-1):
            sum = questions[i][0]
            ind = i + 1 + questions[i][1]
            if ind  < leng: sum += new[ind]
            new[i] = sum
            maximum = max(sum, maximum)
        return maximum
