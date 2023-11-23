class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        store = [ 0, books[0][1]  ]
        for i in range(1, n):
            thick, height = books[i]
            sumThickness = thick
            maxHeight = height
            best = height + store[-1]
            start = i - 1 
            while start >= 0 and sumThickness + books[start][0] <= shelfWidth:
                sumThickness += books[start][0]
                maxHeight = max(maxHeight, books[start][1])
                best = min( best, maxHeight + store[start]   )
                start -= 1
            # print(start)
            store.append(best)
        return store[-1]
                
            
            
        