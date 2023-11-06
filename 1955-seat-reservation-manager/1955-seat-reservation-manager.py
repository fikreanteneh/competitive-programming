class SeatManager:

    def __init__(self, n: int):
        self.seat = [i for i in range(1, n + 1)]
        heapify(self.seat)

    def reserve(self) -> int:
        return heappop(self.seat)

    def unreserve(self, seatNumber: int) -> None:
        heappush(self.seat, seatNumber)
        


# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)