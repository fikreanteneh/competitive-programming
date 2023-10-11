class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        flowers.sort()
        new = [(time, i) for i, time in enumerate(people)]
        new.sort()
        store = defaultdict(int)
        
        for start, end in flowers:
            store[start] += 1
            store[end  + 1] -= 1
        store = sorted(store.items())
        curr = 0
        j = 0
        for time, i in new:
            while j < len(store) and store[j][0] <= time:
                curr += store[j][1]
                j += 1
            people[i] = curr
        return people
            
            