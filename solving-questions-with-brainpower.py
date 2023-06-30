class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        leng = len(questions)
        new = [None]*leng
        for i in range(leng-1,-1,-1):
            sum = questions[i][0]
            ind = i + 1 + questions[i][1]
            if ind  < leng: sum += new[ind]
            new[i] = sum
            if i < leng-1:
                new[i] = max(new[i+1], new[i])
        return new[0]
