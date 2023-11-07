class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        dist = [dis/spe  for dis, spe in zip(dist, speed)]
        dist.sort()
        for time in range(len(dist)):
            if dist[time] <= time:
                return time
        return time + 1