def solution(S):
    n = len(S)
    taken = [set(),set(),set(),set(),set()] 
    
    for i in range(0, n, 2):
        row = ord(S[i]) - ord("A")
        col = int(S[i + 1])
        taken[row].add(col)
        
    ans = 0
    for row in taken:
        consecutive = 0
        print(row)
        for col in range(1, 10):
            if col in row:
                print(col)
                consecutive = 0
                continue
            consecutive += 1
            print(consecutive, "---")
            ans = max(ans, consecutive)
    return ans


print(solution("B3A4C7E6"))

# def solution(S):
#   store = [None]*26
#   ans = []
#   curr = 9
#   for char in S:
#     index = ord(char) - ord("A")
#     if store[index] is not None:
#       ans.append(store[index])
#       continue
#     store[index] = str(curr)
#     ans.append(str(curr))
#     curr -= 1
#   return "".join(ans)


# print(solution("ZXXYYY"))