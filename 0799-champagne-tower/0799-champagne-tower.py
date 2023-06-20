class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        answers = [[poured]]
        for i in range(1, query_row + 1):
            prev = answers[-1]
            rows = [0] * (i + 1)
            if prev[0] > 1:
                rows[0] = (prev[0] - 1)/2
                rows[-1] = (prev[-1] - 1)/2
        
            for j in range(1, i):
                if prev[j-1] > 1:
                    rows[j] += ((prev[j-1] - 1)/2)
                if prev[j] > 1:
                    rows[j] += ((prev[j] - 1)/2)
            answers.append(rows)
        ans = answers[query_row][query_glass]
        return 1 if ans >= 1 else ans