class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        store = {}
        repeated = {}
        neighbor = {}
        neigh = (0, "")
        store[(0, "")] = 1
        
        for lett in t:
            prev = repeated.get(lett, 0)
            store[(prev + 1, lett)] = 0
            store[(0,lett)] = 1
            repeated[lett] = prev + 1
            neighbor[(prev + 1, lett)] = neigh
            neigh = (prev + 1, lett)
            
        for lett in s:
            if lett not in repeated:
                continue
            maxi = repeated[lett]
            for i in range(maxi, -1, -1):
                if (i - 1, lett) in store:
                    store[(i, lett)] += store.get(neighbor[(i, lett)], 0)
        
        return store[neigh]
            
    