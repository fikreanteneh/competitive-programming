class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        
        groups = defaultdict(list)
        for person, gSize in enumerate(groupSizes):
            groups[gSize].append(person)
        
        answer = []
        
        for gSize, persons in groups.items():
            for i in range(0, len(persons), gSize):
                answer.append(persons[i: i + gSize])
        
        return answer
            