class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        
        
        graph = defaultdict(lambda : [0, []])
        for i in range(len(recipes)):
            recipe, ingredient = recipes[i], ingredients[i]
            graph[recipe][0] += len(ingredient)
            for j in ingredient:
                graph[j][1].append(recipe)
            
        answer = []
        supply = set(supplies)
        supplies = deque(supplies)
        while supplies:
            node = supplies.pop()
            if node not in supply:
                answer.append(node)
            for child in graph[node][1]:
                graph[child][0] -= 1
                if graph[child][0] == 0:
                    supplies.appendleft(child)    
        return answer