class Solution:
    def combinationSum(self, list: List[int], num: int) -> List[List[int]]:
        table = []
        table.append([[0]])
        for i in range(1, num + 1):
            if i in list: table.append([[i]])
            else: table.append([])
        for i in range(1, num + 1):
            if len(table[i]) == 0: continue
            for j in list:
                nums = i + j
                if nums <= num:
                    for k in table[i]:
                        new = k + [j]
                        new.sort()
                        if new not in table[nums]: table[nums].append(new)
        return table[num]
