class Solution:
    def racecar(self, target: int) -> int:

        visited = {(0, 1)}
        que = deque([(0, 1, 0)])
        while que:
            pos, speed, instruction = que.pop()
            if pos == target:
                return instruction
            instruction += 1
            accelerate = (pos + speed, speed << 1)
            reverse = (pos, -1 if speed > 0 else 1)
            if accelerate not in visited:
                visited.add(accelerate)
                que.appendleft( (accelerate[0], accelerate[1], instruction) )
            if reverse not in visited:
                visited.add(reverse)
                que.appendleft( (reverse[0], reverse[1], instruction) )
                