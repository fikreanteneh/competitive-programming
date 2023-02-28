class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        for i, pos in enumerate(position):
            position[i] = (pos, speed[i])
        position.sort()
        stack = [0]
        for i in (position[::-1]):
            time = (target - i[0]) / i[1]
            if time > stack[-1]:
                stack.append(time)
        return len(stack) - 1
        