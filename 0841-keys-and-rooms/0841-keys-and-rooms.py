class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        stack = rooms[0].copy()
        visited = set([0])
        while stack:
            curr = stack.pop()
            if curr in visited:
                continue
            visited.add(curr)
            for node in rooms[curr]:
                stack.append(node)
        
        return n == len(visited)