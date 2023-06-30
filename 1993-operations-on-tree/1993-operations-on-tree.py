class LockingTree:

    def __init__(self, parent: List[int]):
        self.graph = defaultdict(lambda: [None, []])
        for i, val in enumerate(parent):
            self.graph[i][0] = val
            self.graph[val][1].append(i)
        self.locked = {}

    def lock(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        self.locked[num] = user
        return True

    def unlock(self, num: int, user: int) -> bool:
        if num not in self.locked or self.locked[num] != user:
            return False
        del self.locked[num]
        return True

    def upgrade(self, num: int, user: int) -> bool:
        if num in self.locked:
            return False
        def linked(node):
            
            if node == -1:
                return True
            if node in self.locked:
                return False
            if linked(self.graph[node][0]):
                return True
        if not linked(num):
            return False
        self.flag = False
        def dfs(node):
            if node in self.locked:
                self.flag = True
                self.locked.pop(node)
            for child in self.graph[node][1]:
                dfs(child)
            return False
        dfs(num)
        if not self.flag: return False
        
        self.locked[num] = user
        return True


# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)