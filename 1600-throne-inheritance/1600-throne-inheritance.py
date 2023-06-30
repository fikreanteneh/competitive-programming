class ThroneInheritance:

    def __init__(self, kingName: str):
        self.graph = defaultdict(list)
        self.graph[kingName] = []
        self.name = kingName

    def birth(self, parentName: str, childName: str) -> None:
        self.graph[parentName].append(childName)
        self.graph[childName] = []

    def death(self, name: str) -> None:
        self.graph[name].append(None)
        

    def getInheritanceOrder(self) -> List[str]:
        order = []
        def solution(name):
            if not name:
                return
            if not self.graph[name] or self.graph[name][-1]:
                order.append(name)
            for child in self.graph[name]:
                solution(child)
                
        solution(self.name)
        return order
            
            
        


# Your ThroneInheritance object will be instantiated and called as such:
# obj = ThroneInheritance(kingName)
# obj.birth(parentName,childName)
# obj.death(name)
# param_3 = obj.getInheritanceOrder()