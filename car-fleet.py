class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        for i in range(len(speed)):
            time = (target - position[i])/speed[i]
            position[i] = (position[i], time)
        position.sort()
        for j in range(len(speed)-1, -1, -1):
            if not stack or stack[-1] < position[j][1]:
                stack.append(position[j][1])
        return len(stack)
