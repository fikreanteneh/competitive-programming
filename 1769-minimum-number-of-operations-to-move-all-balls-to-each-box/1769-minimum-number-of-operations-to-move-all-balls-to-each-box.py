class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n = len(boxes)
        prefix = self.count(boxes, 0, n, 1)
        suffix = self.count(boxes, n-1, -1,-1)
        answer = [0] * n
        for i in range(n):
            answer[i] = prefix[i+1] + suffix[-1-i]
        return answer
    def count(self, boxes, star, end, sign):
        new = [0]
        flag = 0
        for i in range(star, end, sign):
            new.append(new[-1] + flag)
            if boxes[i] == "1":
                flag += 1
        return new
    