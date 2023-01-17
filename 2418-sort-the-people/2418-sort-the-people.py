class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        # Bubble sort
        # n = len(heights)
        # for i in range(n - 1,0,-1):
        #     for j in range(i):
        #         if heights[j] > heights[j+1]:
        #             heights[j], heights[j+1] = heights[j+1], heights[j]
        #             names[j], names[j+1] = names[j+1], names[j]
        # names.reverse()
        # return names
        # Selection sort
        n = len(heights)
        for i in range(n-1):
            temp = heights[i]
            index = i
            for j in range(i+1, n):
                if heights[j] >= temp:
                    index, temp = j, heights[j]
            heights[index], heights[i] = heights[i],heights[index]
            names[index], names[i] = names[i], names[index]
        return names
            