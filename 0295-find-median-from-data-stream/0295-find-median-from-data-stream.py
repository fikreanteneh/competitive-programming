class MedianFinder:

    def __init__(self):
        self.first = [float("inf")]
        self.second = [float("inf")]

        heapify(self.second)
        heapify(self.first)

        self.index = -1
        self.place = [[], self.second, self.first]

    def addNum(self, num: int) -> None:
        # print(self.first, self.second)
        if self.index == 1:
            if self.first[0] * -1 > num:
                heappush(self.first, -1 * num)
                num = heappop(self.first) * -1
            heappush(self.second, num)
        else:
            if self.second[0]  < num:
                heappush(self.second, num)
                num = heappop(self.second)
            heappush(self.first, -1 * num)
        self.index *= -1 
        
    def findMedian(self) -> float:
        # print(self.first, self.second)
        if self.index == 1:
            return -1 * self.first[0]
        return (self.second[0] - self.first[0]) / 2