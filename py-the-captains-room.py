# Enter your code here. Read input from STDIN. Print output to STDOUT 7 lines (7 sloc)  135 Bytes

if __name__ == '__main__':
    k = int(input())
    room = list(map(int, input().split(" ")))
def captainRoom(k, room):
    num = room[0]
    repeated = {}
    for i in room:
        repeated[i] = 1 + repeated.get(i, 0)
    for i in repeated.items():
        if i[1] == 1: 
            print(i[0])
            return
captainRoom(k, room)
