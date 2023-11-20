class UndergroundSystem:

    def __init__(self):
        self.datatracker = defaultdict(lambda: defaultdict(lambda: [0,0] ))
        self.checkInTracker = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkInTracker[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start, t1 = self.checkInTracker.pop(id)
        self.datatracker[start][stationName][1] += 1
        self.datatracker[start][stationName][0] += (t - t1)
        
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        totalTime, totalCars = self.datatracker[startStation][endStation]
        return totalTime / totalCars
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)