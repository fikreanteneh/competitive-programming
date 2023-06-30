class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        
        def operate(temp, operation):
            temp[i % 4] += operation
            temp[i % 4] %= 10
            return tuple(temp)
        
        for i, val in enumerate(deadends):
            deadends[i] = tuple(map(int, list(val)))
        if (0,0,0,0) in deadends:
            return -1
        target = tuple(map(int, list(target)))
        deadends = set(deadends)
        visited = set()
        visited.add((0,0,0,0))
        que = deque([ ((0,0,0,0), 0)])
        operation = 1
        while que:
            curr, level = que.pop()
            if curr == target:
                return level
            curr = list(curr)
            for i in range(8):
                temp = operate(curr.copy(), 1)
                if temp not in visited and temp not in deadends:
                    visited.add(temp)
                    que.appendleft((temp, level + 1))
                temp = operate(curr.copy(), -1)
                
                if temp not in visited and temp not in deadends:
                    visited.add(temp)
                    que.appendleft((temp, level + 1))
                
                    
        return -1
        