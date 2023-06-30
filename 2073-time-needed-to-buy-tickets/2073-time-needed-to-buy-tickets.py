class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        answer = 0
        tickets = deque(tickets)
        flag = True
        while True: #tickets and tickets[k%len(tickets)] != 0:
            
            answer += 1
            # print(k, tickets, answer)
            tickets[0] -= 1
            if tickets[0] == 0:
                if k == 0:
                    break
                tickets.popleft()
                # k -= 1
            else:
                tickets.append(tickets.popleft())
            
            k -= 1
            if k < 0:
                k = len(tickets) - 1  
        return answer
        