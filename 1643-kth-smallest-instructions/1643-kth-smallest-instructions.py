class Solution:
    def kthSmallestPath(self, destination: List[int], k: int) -> str:
        stack = []
        moves = [destination[1], destination[0]]
        factorials = [1]
        for i in range(1, sum(moves) + 1):
            factorials.append(i*factorials[-1])
        def calc(moves):
            return factorials[sum(moves)]//( factorials[moves[0]]*factorials[moves[1]] )
        curr = 0
        for i in range(sum(moves)):
            if moves[0]:
                moves[0] -= 1
                count1 = calc(moves) + curr
                stack.append("H")
                if count1 >= k:
                    continue
                stack.pop()
                moves[0] += 1
            curr = count1
            moves[1] -= 1
            stack.append("V")
        return "".join(stack)