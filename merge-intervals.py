class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        new = []
        new.append(intervals[0])
        for i in intervals:
            flag = True
            for j in range (len(new)):
                if i[0]> new[j][1] or i[1] < new[j][0]:
                    continue
                if new[j][0] > i[0]: new[j][0]= i[0]
                if new[j][1] < i[1]: new[j][1]= i[1]
                flag = False
                break
            if flag: new.append(i)
        return new
